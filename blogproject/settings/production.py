from .common import *
from .globalVar import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','26hyddx2xd_(1^!h4kidh-5i%%h9h*2$84nld!=668fccb(g_y')

ALLOWED_HOSTS = ['localhost','.iwill.fun']
DEBUG = False


# django anymail grid
ANYMAIL = {
    "SENDGRID_API_KEY":" your key",
}
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
DEFAULT_FROM_EMAIL = "bluefeng@iwill.fun"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog2',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
