"""
Configuración ASGI para el proyecto 'core'.

Expone la variable 'application' a nivel de módulo, la cual es utilizada
por los servidores web para comunicarse con tu aplicación.

Para más información, consulta:
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

# Importa el módulo 'os' de Python para interactuar con las variables del sistema operativo.
import os

# Importa la función de Django que genera la interfaz de la aplicación para servidores ASGI.
from django.core.asgi import get_asgi_application

# Establece la variable de entorno predeterminada 'DJANGO_SETTINGS_MODULE'.
# Indica a Django dónde se encuentra el archivo de configuración (settings.py) de tu proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Crea la instancia de la aplicación ASGI.
# Esta es la variable que buscará el servidor (como Daphne o Uvicorn) para "correr" el proyecto.
application = get_asgi_application()