from django.apps import AppConfig


class InventarioConfig(AppConfig):
    name = 'inventario'
    verbose_name = "Aplicacion inventario y administracion de ventas"

    def ready(self):
        pass

