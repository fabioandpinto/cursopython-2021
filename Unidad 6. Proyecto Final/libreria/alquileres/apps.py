from django.apps import AppConfig


class AlquileresConfig(AppConfig):
    name = 'alquileres'

    def ready(self):
        import alquileres.signals