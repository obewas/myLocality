from django.apps import AppConfig


class VotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hood'

    def ready(self):
        from . import signals
