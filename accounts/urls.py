from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import RedirectView

from .views import profile_view, signup_view

urlpatterns = [
    path('register/', RedirectView.as_view(pattern_name='signup', permanent=False), name='register'),
    path('signup/', signup_view, name='signup'),
    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
]