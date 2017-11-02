from django.conf.urls import url
from apps.homepage import views

urlpatterns = [
    url(r'^fail500/$', views.fail500, name='fail500'),
    url(r'^highlights/$', views.highlights, name='highlights'),
    url(r'^set-units/?$', views.set_units, name='set_units'),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<coin_symbol>[-\w]+)/$', views.coin_overview, name='coin_overview'),
]


