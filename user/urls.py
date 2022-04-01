from django.urls import path
from . import views

urlpatterns = [

    path('', views.LoginView.as_view(), name="login"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('verification', views.OTPVerify.as_view(), name="verification"),
    path('logout', views.LogoutView, name="logout"),
    ########### forgot password urls################################
    path('otp-send', views.PasswordOtpSendView.as_view(), name="otp-send"),
    path('email-otp-send', views.PasswordOTPVerifyView.as_view(), name="password-otp"),
    path('new-password', views.NewPasswordView.as_view(), name="new-password"),
    ########### forgot password urls end################################

]