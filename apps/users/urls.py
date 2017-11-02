from django.conf.urls import url
from apps.users import views

urlpatterns = [
    url(r'^signup/?$', views.signup, name='signup'),
    url(r'^login/?$', views.user_login, name='user_login'),
    url(r'^logout/?$', views.logout_request, name='logout_request'),
    url(r'^confirm/(?P<verif_code>[-\w]+)/$', views.confirm_subscription, name='confirm_subscription'),
    url(r'^unconfirmed-email/?$', views.unconfirmed_email, name='unconfirmed_email'),
    url(r'^confirm-pw-reset/(?P<email_address>[-\w@.+]+)?$', views.confirm_pw_reset, name='confirm_pw_reset'),
    url(r'^set-password/?$', views.password_upsell, name='password_upsell'),
    url(r'^change-password/?$', views.change_password, name='change_password'),
    url(r'^forgot-password/?$', views.forgot_password, name='forgot_password'),
    url(r'^reset-pw/(?P<verif_code>[-\w@.+]+)?$', views.reset_pw, name='reset_pw'),
    url(r'^$', views.dashboard, name='dashboard'),
]
