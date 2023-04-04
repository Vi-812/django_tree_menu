from django.contrib import admin
from .models import TreeMenu


class MenuAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'uri',
        'parent',
        'position',
    ]


admin.site.register(TreeMenu, MenuAdmin)
