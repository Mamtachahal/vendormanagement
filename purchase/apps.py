from django.apps import AppConfig


class PurchaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'purchase'

    def ready(self) -> None:
        import purchase.signals
        # return super().ready()