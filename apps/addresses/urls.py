from django.conf.urls import url
from apps.addresses import views

urlpatterns = [
    # Users
    url(r'^unsubscribe/(?P<unsub_code>[-\w]+)/$', views.unsubscribe_address, name='unsubscribe_address'),
    url(r'^remove-subscription/(?P<address_subscription_id>[-\w]+)/$', views.user_unsubscribe_address, name='user_unsubscribe_address'),
    url(r'^archive-forwarding-address/(?P<address_forwarding_id>[-\w]+)/$', views.user_archive_forwarding_address, name='user_archive_forwarding_address'),

    # Webhooks:
    url(r'^address-webhook/(?P<secret_key>[-\w]+)/(?P<ignored_key>[-\w]+)?$', views.address_webhook, name='address_webhook'),

    # App pages
    url(r'^(?P<coin_symbol>[-\w]+)/forwarding/$', views.setup_address_forwarding, name='setup_address_forwarding'),
    url(r'^(?P<coin_symbol>[-\w]+)/subscribe/$', views.subscribe_address, name='subscribe_address'),
    url(r'^(?P<coin_symbol>[-\w]+)/address/(?P<address>[-\w]+)/$', views.address_overview, name='address_overview'),
    url(r'^(?P<coin_symbol>[-\w]+)/address/(?P<address>[-\w]+)/(?P<wallet_name>[-\w\.]+)/$', views.address_overview, name='address_overview'),

    # Widget
    url(r'^widgets/(?P<coin_symbol>[-\w]+)/?$', views.search_widgets, name='search_widgets'),
    url(r'^show-widgets/(?P<coin_symbol>[-\w]+)/(?P<address>[-\w]+)/$', views.widgets_overview, name='widgets_overview'),
    url(r'^widget/(?P<coin_symbol>[-\w]+)/(?P<address>[-\w]+)/balance/$', views.render_balance_widget, name='render_balance_widget'),
    url(r'^widget/(?P<coin_symbol>[-\w]+)/(?P<address>[-\w]+)/received/$', views.render_received_widget, name='render_received_widget'),

    # Forwarding Pages (URL hacks)
    url(r'^widgets/$', views.widget_forwarding, name='widget_forwarding'),
    url(r'^forwarding/$', views.forward_forwarding, name='forward_forwarding'),  # awesome name
    url(r'^subscribe/$', views.subscribe_forwarding, name='subscribe_forwarding'),

]



