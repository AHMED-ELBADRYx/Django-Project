from django.contrib import admin
from .models import Female, Male, User, Product, Video, Login

# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_display_links = ('email',)
    list_editable = ('message',)
    search_fields = ('name',)
    list_filter = ('password',)
    fields = ('message',)

admin.site.register(Female)
admin.site.register(Male)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Video)
admin.site.register(Login, LoginAdmin)
admin.site.site_header = "My Admin Panel"
admin.site.site_title = "Admin Panel"