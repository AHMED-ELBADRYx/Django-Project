from django.contrib import admin
from .models import Product, Test
# Register your models here.

admin.site.register(Product)
admin.site.register(Test)
admin.site.site_header = "My Admin Panel"
admin.site.site_title = "Admin Panel"
