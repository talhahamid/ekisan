from django.apps import AppConfig


class DealerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dealer'


class DealerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dealer'

    def ready(self):
        import dealer.signals 