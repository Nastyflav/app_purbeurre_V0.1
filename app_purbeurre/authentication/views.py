from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from .forms import SignUpForm


class SignUp(FormView):
    """Show form and create user if valid."""

    form_class = SignUpForm
    success_url = '/'
    template_name = 'authentication/account_creation.html'

    def form_valid(self, form):
        """ if form is valid """

        form.save()
        email = form.cleaned_data.get('email')
        _password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=_password)
        if user:
            login(self.request, user)
        return super().form_valid(form)


def profile(request):
    """ Account profile """

    return render(request, "authentication/user_profile.html")