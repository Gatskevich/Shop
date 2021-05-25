from django.conf.urls import url, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url('register/', user_views.register, name='register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    url(r'^password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^activate/<uidb64>/<token>', user_views.activate, name='activate'),
    url(r'^send/<int:user_id>/', user_views.send, name='admin_email_message'),
]