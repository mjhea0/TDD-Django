from pyvows import Vows, expect

from django_pyvows.context import DjangoContext, DjangoHTTPContext
from selenium import webdriver

def onBrowser(webdriver):
    class BrowserTests(DjangoHTTPContext):
    
        def topic(self):
            webdriver.get(self.get_url("/"))
            return webdriver
        
        def teardown(self):
            webdriver.quit()

        def should_prompt_the_user_with_a_login_page(self, topic):
            expect(topic.title).to_include('Django')

    return BrowserTests

@Vows.batch
class TDDDjangoApp(DjangoHTTPContext):

    def get_settings(self):
        return "tddapp.settings"

    def topic(self):
        self.start_server()
        #manual add some more threads to the CherryPy server
        self.server.thr.server.requests.grow(3)
    
    def teardown(self):
        #clean up the threads so we can exit cleanly
        self.server.thr.server.requests.stop(timeout=1)

    class OnChrome(onBrowser(webdriver.Chrome())):
        pass
    
    class OnFirefox(onBrowser(webdriver.Firefox())):
        pass

    class OnPhantonJS(onBrowser(webdriver.PhantomJS())):
        pass
        
