"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

# Importa el módulo del sistema operativo
import os

# Importa la función específica para aplicaciones WSGI
from django.core.wsgi import get_wsgi_application

# Establece cuál es el archivo de configuración que debe leer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Crea la variable application necesaria para que el servidor funcione
application = get_wsgi_application()