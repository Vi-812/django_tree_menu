# from django import template
#
# register = template.Library()
#
#
#
#
#
#
#
#
#
#
# from django.conf import settings
#
#
#
# @register.filter
# def getattribute(obj, option):
#     current = {}
#     for item in settings.THEMENU:
#         try:
#             current = getattr(obj, item)
#             if option == 'menu_url':
#                 obj = obj.get_absolute_url()
#             elif option == 'menu_name':
#                 obj = obj.name
#             elif option == 'menu_css':
#                 obj = obj.css_class
#             elif option == 'get_url':
#                 obj = current.get_absolute_url()
#             else:
#                 obj = getattr(current, option)
#         except:
#             pass
#     return obj
#
# # Сам тег просто извлекает значения из базы. Координирует всю логику фильтр getattribute
# @register.inclusion_tag('menu.html')
# def get_menu(position):
#     menu = Menu.objects.filter(
#         menu__position=position,
#         menu__visible=1,
#         visible=1,
#     ).order_by('tree_id')
#     if menu:
#         return {'menu': menu}
#     else:
#         raise template.TemplateSyntaxError()
