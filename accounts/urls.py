from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView, LoginView



urlpatterns = [
    path('login/',  LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #Substituido por message.sucess
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
]