from django.shortcuts import render


def index(request):
    return render(request, 'tree_menu/index.html')
