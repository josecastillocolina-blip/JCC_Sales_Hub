"""
Configuración de URLs para el proyecto 'core'.

La lista `urlpatterns` enruta las URLs hacia las "views" (vistas). 
"""

# Importa el módulo de administración de Django.
from django.contrib import admin

# 'path' sirve para definir rutas simples.
# 'include' sirve para conectar las rutas de otras carpetas (apps) a este archivo principal.
from django.urls import path, include 

urlpatterns = [
    # Ruta para el panel de administración (por defecto: http://127.0.0.1:8000/admin/).
    path('admin/', admin.site.urls),

    # Ruta raíz (vacía ''). 
    # Al dejar las comillas vacías, significa que cuando entres a la página principal 
    # (ej. www.tuweb.com), Django buscará las rutas dentro de la carpeta 'ventas'.
    path('', include('ventas.urls')), 
]