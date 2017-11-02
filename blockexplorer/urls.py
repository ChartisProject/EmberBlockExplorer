from django.conf.urls import include, url
from django.contrib import admin
from apps.transactions import views as transactions_views


urlpatterns = [
    # Logging Test

    # Admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^u/', include('apps.users.urls')),
    url(r'^', include('apps.addresses.urls')),
    url(r'^', include('apps.transactions.urls')),
    url(r'^', include('apps.blocks.urls')),
    url(r'^', include('apps.wallets.urls')),
    url(r'^', include('apps.metadata.urls')),
    url(r'^', include('apps.wallets.urls')),
    url(r'^', include('apps.homepage.urls')),
]
