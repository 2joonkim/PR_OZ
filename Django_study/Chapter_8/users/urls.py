from django.urls import path
from users.cb_views import SignupView, LoginView, verify_email
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='cbv_signup'),
    path('login/', LoginView.as_view(), name='cbv_login'),
    path('logout/', LogoutView.as_view(), name='cbv_logout'),
    path('verify/', verify_email, name='verify_email'),
]