import os
from pathlib import Path

# Define la ruta base del proyecto. 
# Ayuda a encontrar archivos usando rutas relativas en lugar de rutas fijas.
BASE_DIR = Path(__file__).resolve().parent.parent

# ¡CUIDADO! Esta es la clave maestra para la seguridad de tu web (firmas de sesiones, tokens, etc.)
# Nunca la compartas en producción ni la subas a repositorios públicos.
SECRET_KEY = 'django-insecure-)c2j6z9&7-!nz@25$d7@a4i78unj$uao&c*^82(&fq27^j49i9'

# Si está en True, verás errores detallados. En producción DEBE ser False.
DEBUG = True

# Lista de dominios o IPs donde tu web puede funcionar (ej. ['www.tuweb.com']).
ALLOWED_HOSTS = []

# Apps instaladas. Incluye las propias de Django y las tuyas (como 'ventas').
INSTALLED_APPS = [
    'django.contrib.admin',        # Interfaz de administración
    'django.contrib.auth',         # Sistema de autenticación (usuarios)
    'django.contrib.contenttypes', # Permisos de modelos
    'django.contrib.sessions',     # Manejo de sesiones
    'django.contrib.messages',     # Mensajes temporales (notificaciones)
    'django.contrib.staticfiles',  # Manejo de archivos CSS, JS e imágenes
    'ventas',                      # Tu aplicación personalizada de ventas
]

# Capas intermedias que procesan las peticiones antes de llegar a la vista.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',             # Protección contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Vincula usuarios a peticiones
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Indica dónde está el archivo principal de rutas (URLs).
ROOT_URLCONF = 'core.urls'

# Configuración del motor de plantillas (HTML).
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],             # Carpetas adicionales donde buscar HTML
        'APP_DIRS': True,       # Busca carpetas "templates" dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Indica qué archivo usar para servidores tradicionales (sincrónicos).
WSGI_APPLICATION = 'core.wsgi.application'

# Configuración de la base de datos (aquí estás usando PostgreSQL).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jcc_sales_hub_db',   # Nombre de tu base de datos en Postgres
        'USER': 'postgres',           # Tu usuario de base de datos
        'PASSWORD': 'kevin2001',      # Tu contraseña (¡ten cuidado al compartirla!)
        'HOST': '127.0.0.1',          # Dirección local
        'PORT': '5432',               # Puerto por defecto de PostgreSQL
    }
}

# Reglas para validar que las contraseñas de los usuarios sean seguras.
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración de idioma y zona horaria.
LANGUAGE_CODE = 'en-us' # Podrías cambiarlo a 'es-es' o 'es-mx' para español
TIME_ZONE = 'UTC'       # Zona horaria
USE_I18N = True         # Habilita el sistema de traducción
USE_TZ = True           # Habilita el soporte para zonas horarias

# URL para acceder a archivos estáticos (CSS, JavaScript, imágenes de diseño).
STATIC_URL = 'static/'