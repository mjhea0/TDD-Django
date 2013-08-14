from pyvows import Vows, expect

from django_pyvows.context import DjangoContext, DjangoHTTPContext
from selenium import webdriver

@Vows.batch
class TDDDjangoApp(DjangoContext):

    '''This function returns the BrowserTests class which implements
    all the test we want to test.  Pass in the webdriver type and port
    for the django server to run on to setup the context of the tests
    so you can run them against different browsers
    '''
    def onBrowser(webdriver, port):
        class BrowserTests(DjangoHTTPContext):
        
            def get_settings(self):
                return "tddapp.settings"

            def topic(self):
                self.start_server(port=port)
                browser = webdriver()
                browser.get(self.get_url("/"))
                return browser

            def should_prompt_the_user_with_a_login_page(self, topic):
                expect(topic.title).to_include('Django')

        return BrowserTests

    class OnChrome(onBrowser(webdriver.Chrome, 8887)):
        pass
    
    class OnFirefox(onBrowser(webdriver.Firefox, 8888)):
        pass

    class OnPhantonJS(onBrowser(webdriver.PhantomJS, 8886)):
        pass
        
