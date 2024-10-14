from django.urls import path
from .views import pagina_inicial, criacao_wishlist, comprar_creditos, ver_wishlist
urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('criar/', criacao_wishlist, name='criacao_wishlist'),
    path('comprar/', comprar_creditos, name='comprar_creditos'),
    path('ver/<int:wishlist_id>/', ver_wishlist, name='ver_wishlist'),
]
