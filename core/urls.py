from django.urls import path
from core.views import full_menu_render, menu_render, menu_render_without_slug

urlpatterns = [
    path('full-menu/', full_menu_render, name='show_full_menu_page'),
    path('<slug:slug>/', menu_render, name='show_menu_page_v2'),
    path('', menu_render_without_slug, name='show_menu_page_v2'),
]
