from django.urls import path
from . import views

urlpatterns = [
    # 1. Pantalla de inicio (Login)
    path("", views.login_view, name="login"),
    # 2. Pantalla para que los clientes se registren
    path("registro/", views.registro_view, name="registro"),
    # 3. El Tablero principal (Solo Master/Jose)
    path("home/", views.home_view, name="home"),
    # 4. NUEVA: La Bienvenida exclusiva del Cliente
    path("cliente/", views.cliente_view, name="cliente"),
    # 5. El Punto de Venta (Tu módulo de facturación Master)
    path("punto-venta/", views.pos_view, name="ventas"),
]
