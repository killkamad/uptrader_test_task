from django import template
from django.utils.html import format_html
from core.models import MenuItem
from core.utils.html import create_html
from core.utils.tree_node import TreeNode

register = template.Library()


@register.simple_tag
def draw_menu(slug):
    if slug is None:
        menu_item = MenuItem.objects.select_related('parent').order_by('name').filter(parent__isnull=True).first()
    else:
        menu_item = MenuItem.objects.select_related('parent').order_by('name').get(slug=slug)
    active_tree = TreeNode(data=menu_item, select=True)
    active_tree.children += map(lambda x: TreeNode(x), menu_item.children.all())
    menu_data = create_menu(menu_item, active_tree)
    html = create_html(menu_data)
    return format_html(html)


def create_menu(active_item, active_tree):
    active_tree.children.sort(key=lambda x: x.data.name)
    parent = active_item.parent
    if parent is None:
        return active_tree
    scan_for_children = map(lambda x: TreeNode(x), parent.children.all().exclude(id=active_item.id))
    parent_tree = TreeNode(parent)
    parent_tree.children += scan_for_children if scan_for_children else []
    parent_tree.children.append(active_tree)
    return create_menu(parent, parent_tree)

