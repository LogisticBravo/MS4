"""
Subclasses to override allauth forms so at to
allow for two forms on the same page for login and signup page.
direction from:
https://stackoverflow.com/questions/29499449/django-allauth-login-signup-form-on-homepage
"""
from allauth.account.views import SignupView, LoginView
from allauth.account.forms import LoginForm, SignupForm
# Create your views here.


class CustomSignupView(SignupView):
    """ Takes existing context of the SignupView and add's the login form
    to the context to be used
    """
    # here we add some context to the already existing context
    def get_context_data(self, **kwargs):
        # we get context data from original view
        context = super(CustomSignupView,
                        self).get_context_data(**kwargs)
        context['login_form'] = LoginForm()  # add form to context
        return context


signup = CustomSignupView.as_view()


class CustomLoginView(LoginView):
    """ Takes existing context of the LoginView and add's the signup form
     to the context to be used
    """
    # here we add some context to the already existing context
    def get_context_data(self, **kwargs):
        # we get context data from original view
        context = super(CustomLoginView,
                        self).get_context_data(**kwargs)
        context['signup_form'] = SignupForm()  # add form to context
        return context


login = CustomLoginView.as_view()
