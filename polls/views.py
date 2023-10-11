from django.shortcuts import render
from .models import MainMenu
from django.db import connection


def get_category_nav(request, categories=None, menu_name=None):
    if categories is None:
        categories = MainMenu.objects.filter(main_menu=None,
                                             menu__name=menu_name)
        categories[0].active = True
    else:
        yield 'in'

    for category in categories:
        yield category
        subcats = MainMenu.objects.select_related().filter(main_menu=category)
        if len(subcats):
            category.leaf = False
            for x in get_category_nav(request, subcats):
                yield x
        else:
            category.leaf = True
    yield 'out'


def index(request):
    mmenu = MainMenu.objects.filter(menu__name='Main')
    cq = connection.queries
    path = request.path
    path_raw = path.replace('/', '')
    context = {
        'mmenu': mmenu,
        'cq': cq,
        'path': path,
        'path_raw': path_raw,
    }
    return render(request, 'index.html', context)


def menu_link(request, slug):
    post = MainMenu.objects.get(slug=slug)
    path = request.path
    path_raw = path.replace('/', '')
    context = {
        'post': post,
        'path_raw': path_raw,
        }
    return render(request, 'menu_link.html', context)
