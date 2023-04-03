from django.contrib import admin
from .models import TreeMenu


class MenuAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'uri',
        'parent',
    ]
    mptt_level_indent = 20


admin.site.register(TreeMenu, MenuAdmin)
