from django.urls import reverse


def create_html(tree):
    menu_html = '<ul>'
    url = create_url("show_menu_page_v2", tree.data.slug)
    if tree.select is True:
        menu_html += f'<li>{tree.data}</li>'
    else:
        menu_html += f'<li><a href="{url}">{tree.data}</a></li>'
    menu_html += create_submenu_html(tree)
    return menu_html


def create_submenu_html(tree):
    submenu_html = '<ul>'
    for child in tree.children:
        if child.select is True:
            submenu_html += f'<li>{child.data.name}'
        else:
            url = create_url("show_menu_page_v2", child.data.slug)
            submenu_html += f'<li><a href="{url}">{child.data.name}</a>'
        submenu_html += create_submenu_html(child)
        submenu_html += '</li>'
    submenu_html += '</ul>'
    return submenu_html


def create_url(url_name, *args):
    return reverse(url_name, args=[*args])
