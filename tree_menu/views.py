from django.shortcuts import render
from .models import TreeMenu


def index(request):
    return render(request, 'templatetags/menu.html', {'menu': TreeMenu.objects.all()})
