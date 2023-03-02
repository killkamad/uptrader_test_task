from django.contrib import admin
from core.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
