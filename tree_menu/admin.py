from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Menu


class CategoryAdmin(MPTTModelAdmin):
    fields = ['name', 'uri', 'parent']
    mptt_level_indent = 20


admin.site.register(Menu, CategoryAdmin)
