from django.shortcuts import render

from djangoApp.models import MenuItem


def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(
        name=menu_name).select_related('group')
    return render(request, 'menu.html', {'menu_items': menu_items})
