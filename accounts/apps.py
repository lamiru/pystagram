from django.apps import AppConfig as DjangoAppConfig
from accounts.signals import app_ready

class AppConfig(DjangoAppConfig):
    name = 'accounts'
    verbose_name = 'Accounts'

    def ready(self):
        app_ready.send(sender=self)
