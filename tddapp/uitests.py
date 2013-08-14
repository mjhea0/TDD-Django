from pyvows import Vows, expect

from django_pyvows.context import DjangoContext, DjangoHTTPContext
from selenium import webdriver

@Vows.batch
class TDDDjangoApp(DjangoContext):

    
    class OnFirefox(DjangoHTTPContext):
        
        def get_settings(self):
            return "tddapp.settings"

        def topic(self):
            self.start_server(port=8888)
            browser = webdriver.Firefox()
            browser.get(self.get_url("/"))
            return browser

        def should_prompt_the_user_with_a_login_page(self, topic):
            expect(topic.title).to_include('Login')
    
    class OnChrome(DjangoHTTPContext):
        
        def get_settings(self):
            return "tddapp.settings"

        def topic(self):
            self.start_server(port=8887)
            browser = webdriver.Chrome()
            browser.get(self.get_url("/"))
            return browser

        def should_prompt_the_user_with_a_login_page(self, topic):
            expect(topic.title).to_include('Django')

