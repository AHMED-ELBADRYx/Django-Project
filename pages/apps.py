from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal' # Layout can be 'horizontal' or 'vertical'
    # menu = 'pages.menu.Menu'  # Assuming you have a custom menu defined in pages/menu.py
    # admin_name = 'My Admin Panel'
    # site_header = 'My Admin Panel'
    # site_title = 'Admin Panel'
    # index_title = 'Welcome to the Admin Panel'