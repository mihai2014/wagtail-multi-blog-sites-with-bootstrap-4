from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#uf)=w+ui#y=o_pbba1@wk#&!5fnv1ts4ujj@mz62*5b$qkl-k'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*','localhost','mihaicorciu.ro'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
