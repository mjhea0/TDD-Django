from pyvows import Vows, expect
from django_pyvows.context import DjangoHTTPContext 

DjangoHTTPContext.start_environment("tddapp.settings")

from accounts.views import login
from django.template.loader import render_to_string

@Vows.batch
class LoginPageVows(DjangoHTTPContext):

    def topic(self):
        self.start_server()

    class LoginPageURL(DjangoHTTPContext):

        def topic(self):        
             return self.url("^login/$")

        def url_should_be_mapped_to_login_view(self, topic):
            expect(topic).to_match_view(login)

    class LoginPageView(DjangoHTTPContext):

        def topic(self):
            return login(self.request())

        def should_return_valid_HTTP_Response(self,topic):
            expect(topic).to_be_http_response()

        def should_return_login_page(self, topic):
            loginTemplate = render_to_string("login.html")
            expect(topic.content.decode()).to_equal(loginTemplate)

    class LoginPageTemplate(DjangoHTTPContext):

        def topic(self):
            return self.template("login.html", {"referrer":"Facebook"})

        def should_have_login_form(self, topic):
            expect(topic).to_contain("#login-form")

        def should_have_username_field(self,topic):
            expect(topic).to_contain("#username")

        def should_use_password_field(self,topic):
            expect(topic).to_contain("#password[type='password']")

        def should_not_have_settings_link(self,topic):
            expect(topic).Not.to_contain("a#settings")

        class WelcomeMessage(DjangoHTTPContext):

            def topic(self, loginTemplate):
                return loginTemplate.get_text('h1')

            def should_welcome_user_from_referrer(self, topic):
                expect(topic).to_equal("Welcome Facebook user. Please login.")