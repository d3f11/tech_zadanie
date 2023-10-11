from django import template

from django.template.defaultfilters import stringfilter
from ..models import MainMenu
from ..views import get_category_nav

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    if not menu_name:
        return
    request = context['request']
    menu_name_data = MainMenu.objects.filter(menu__name=menu_name)
    data = get_category_nav(menu_name_data, menu_name=menu_name)

    return {'data': data,
            'request': request,
            'menu_name': menu_name}


@register.filter(name='slashes')
@stringfilter
def slashes(value):
    return f'/{value}/'
