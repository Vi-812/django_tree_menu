from django import template
from tree_menu.models import MenuItem
register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_menu(context):
    menu_items = MenuItem.objects.filter(level=0)
    return {
        "menu_items": menu_items,
    }
