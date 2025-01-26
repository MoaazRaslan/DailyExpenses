from django.urls import path
from django.contrib.auth import views as auth_view
from . import views as user_view

urlpatterns = [
    path('login/',auth_view.LoginView.as_view(template_name = 'user/login.html'),name='login'),
    path('register/',user_view.register_view,name='register')   ,
    path('logout/',auth_view.LogoutView.as_view(template_name = 'user/logout.html'),name='logout'),
    path('reset-password/',auth_view.PasswordResetView.as_view(),name='password_reset'), 
    path('reset-password-done/',auth_view.PasswordResetDoneView.as_view(),name='password_reset_done'), 
    path('reset-password-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'), 
    path('reset-password-complete/',auth_view.PasswordResetCompleteView.as_view(),name='password_reset_complete'), 
]
