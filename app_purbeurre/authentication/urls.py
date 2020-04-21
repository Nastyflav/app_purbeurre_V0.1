from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm

app_name = 'authentication'

urlpatterns = [
    path('', LoginView.as_view(authentication_form=SignUpForm), name="login"),
    path('deconnexion/', LogoutView.as_view(), name="logout"),
    path('inscription/', views.SignUp.as_view(), name="signup"),
    path('profil/', views.profile, name="profile"),
]