from django.conf.urls import url
from apps.blocks import views

urlpatterns = [
    url(r'^latest-block/$', views.latest_block_forwarding, name='latest_block_forwarding'),
    url(r'^(?P<coin_symbol>[-\w]+)/block/(?P<block_representation>[-\w]+)/$', views.block_overview, name='block_overview'),
    url(r'^(?P<coin_symbol>[-\w]+)/latest-block/$', views.latest_block, name='latest_block'),
    url(r'^(?P<coin_symbol>[-\w]+)/block/(?P<block_num>[\d]+)/(?P<tx_num>[\d]+)/$', views.block_ordered_tx, name='block_ordered_tx'),
]