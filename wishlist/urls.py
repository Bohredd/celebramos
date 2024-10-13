
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='home_pt'), # em portugues
    path('en/', views.homeview, name='home_en'), # em ingles
    path('cw/<str:tipo>/<int:site_id>/', views.criar_site, name='wishlist_criar'),
    path("site/criar/", views.criar_site, name="site_criar"),
    path('base/', views.base, name='base'),
    path("checkout/<str:tipo>", views.checkout, name="checkout"),
    path("compartilhar/", views.gerar_qr_code_compartilhamento, name="compartilhar"),
    path("wishlist/ver/<int:site_id>/", views.ver_lista, name="ver_site"),
    path("wishlists/", views.tipos_wishlist, name="tipos_wishlist"),
    path("wishlists/minhas", views.minhas_wishlists, name="minhas_wishlists"),
    path("wishlist/<int:wishlist_id>/", views.wishlist_detalhes, name="detalhes"),
]
