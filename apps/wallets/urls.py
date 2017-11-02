from django.conf.urls import url
from apps.wallets import views

urlpatterns = [
    url(r'^(?P<coin_symbol>[-\w]+)/xpub/(?P<pubkey>[-\w]+)/$', views.wallet_overview, name='wallet_overview_default'),
]