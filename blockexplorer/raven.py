# Raven client that does nothing if there is no SENTRY_DSN (e.g. localhost)

from django.conf import settings
from raven import Client

client = Client(settings.SENTRY_DSN)
