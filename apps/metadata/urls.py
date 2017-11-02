from django.conf.urls import url
from apps.metadata import views

urlpatterns = [
    url(r'^(?P<coin_symbol>[-\w]+)/metadata/address/(?P<address>[-\w]+)/$', views.add_metadata_to_address, name='add_metadata_to_address'),
    url(r'^(?P<coin_symbol>[-\w]+)/metadata/tx/(?P<tx_hash>[-\w]+)/$', views.add_metadata_to_tx, name='add_metadata_to_tx'),
    url(r'^(?P<coin_symbol>[-\w]+)/metadata/block/(?P<block_hash>[-\w]+)/$', views.add_metadata_to_block, name='add_metadata_to_block'),
    url(r'^metadata/(?P<coin_symbol>[-\w]+)/(?P<identifier_type>[\w]+)/(?P<identifier>[-\w]+)/$', views.poll_metadata, name='poll_metadata'),
    url(r'^metadata/$', views.metadata_forwarding, name='metadata_forwarding'),
    url(r'^(?P<coin_symbol>[-\w]+)/metadata/$', views.add_metadata, name='add_metadata'),
]