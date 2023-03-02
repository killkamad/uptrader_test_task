from django import template
from django.utils.html import format_html
from core.models import MenuItem

register = template.Library()


# Отрисовка полностью раскрытого меню
@register.simple_tag
def draw_full_menu():
    menu_item = MenuItem.objects.get(name='Menu')
    menu_html = '<ul>'
    if menu_item.parent_id is None:
        menu_html += f'<li>{menu_item.name} - {menu_item.id}'
        menu_html += draw_full_submenu(menu_item)
        menu_html += '</li>'
    menu_html += '</ul>'
    return format_html(menu_html)


def draw_full_submenu(menu_item):
    submenu_html = ''
    if menu_item.children.exists():
        submenu_html += '<ul>'
        for child in menu_item.children.all():
            submenu_html += ''
            submenu_html += f'<li>{child.name} - {child.id}'
            submenu_html += draw_full_submenu(child)
            submenu_html += '</li>'
        submenu_html += '</ul>'
    return submenu_html