from django.conf.urls import url
from apps.transactions import views

urlpatterns = [
    url(r'^(?P<coin_symbol>[-\w]+)/tx/(?P<tx_hash>[-\w]+)/$', views.transaction_overview, name='transaction_overview'),
    url(r'^(?P<coin_symbol>[-\w]+)/pushtx/$', views.push_tx, name='push_tx'),
    url(r'^(?P<coin_symbol>[-\w]+)/decodetx/$', views.decode_tx, name='decode_tx'),
    url(r'^(?P<coin_symbol>[-\w]+)/embed-data/$', views.embed_txdata, name='embed_txdata'),

    url(r'^(?P<coin_symbol>[-\w]+)/tx-confidence/(?P<tx_hash>[-\w]+)/$', views.poll_confidence, name='poll_confidence'),

    url(r'^pushtx/$', views.pushtx_forwarding, name='pushtx_forwarding'),
    url(r'^decodetx/$', views.decodetx_forwarding, name='decodetx_forwarding'),
    url(r'^embed-data/$', views.embed_txdata_forwarding, name='embed_txdata_forwarding'),
    url(r'^latest-unconfirmed-tx/$', views.latest_unconfirmed_tx_forwarding, name='latest_unconfirmed_tx_forwarding'),
    url(r'^(?P<coin_symbol>[-\w]+)/latest-unconfirmed-tx/$', views.latest_unconfirmed_tx, name='latest_unconfirmed_tx'),
]



