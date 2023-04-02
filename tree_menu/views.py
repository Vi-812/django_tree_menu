from django.shortcuts import render
from .models import Menu


def index(request):
    return render(request, 'templatetags/menu.html', {'menu': Menu.objects.all()})
