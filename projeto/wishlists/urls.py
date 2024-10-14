from django.urls import path
from .views import pagina_inicial, criacao_wishlist, comprar_creditos, ver_wishlist_cliente, compartilhar_wishlist, ver_wishlist_convidado
urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('criar/', criacao_wishlist, name='criacao_wishlist'),
    path('comprar/', comprar_creditos, name='comprar_creditos'),
    path('ver/<int:wishlist_id>/', ver_wishlist_cliente, name='ver_wishlist'),
    path('ver/c/<int:wishlist_id>/', ver_wishlist_convidado, name='ver_wishlist_convidado'),
    path('compartilhar/<int:wishlist_id>/', compartilhar_wishlist, name='compartilhar_wishlist'),
]
