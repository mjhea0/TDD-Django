from pyvows import Vows, expect

from django_pyvows.context import DjangoHTTPContext
from selenium import webdriver

@Vows.batch
class TDDDjangoApp(DjangoHTTPContext):

    def get_settings(self):
        return "tddapp.settings"

    def topic(self):
        self.start_server()
        browser = webdriver.Firefox()
        browser.get(self.get_url("/"))
        return browser

    def should_prompt_the_user_with_a_login_page(self, topic):
        expect(topic.title).to_include('Login')
