from django.shortcuts import render


def menu_render(request, slug):
    return render(request, 'menu.html', {'slug': slug})


def menu_render_without_slug(request):
    return render(request, 'menu.html', {'slug': None})


def full_menu_render(request):
    return render(request, 'full_menu.html')
