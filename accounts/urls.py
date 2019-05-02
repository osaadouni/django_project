from django.urls import path, include 
from django.conf.urls import  url
from django.contrib.auth import views as auth_views

from . import views as accounts_views 

app_name = 'accounts'

urlpatterns = [
    path('', accounts_views.UserDetailView.as_view(), name='account_profile'), 
    #path('signup/', accounts_views.signup, name='signup'),
    path('signup/', accounts_views.UserCreateView.as_view(), name='signup'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), 
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), 

    url(r'^password_reset/$', 
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html', 
            subject_template_name='accounts/password_reset_subject.txt'
        ),
        name='password_reset'),

    url(r'^password_reset/done/$', 
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),

    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),

    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^password_change/$', 
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/password_change.html', 
            success_url='/accounts/password_change/done/'
        ),
        name='password_change'
    ), 

    url(r'^password_change/done/$', 
        auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'), 
   
    url(r'^profile/$', accounts_views.UserDetailView.as_view(), name='account_profile'), 
    url(r'^profile/edit/$', accounts_views.UserUpdateView.as_view(), name='account_edit'),


]
  
