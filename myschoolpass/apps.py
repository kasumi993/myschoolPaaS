from django.apps import AppConfig


class MyschoolpassConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myschoolpass'
    def ready(self):
            import myschoolpass.signals
