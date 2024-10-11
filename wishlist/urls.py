
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeview, name='home_pt'), # em portugues
    path('en/', views.homeview, name='home_en'), # em ingles
    path('cw/<str:tipo>', views.criar_site, name='wishlist_criar'),
    path('base/', views.base, name='base'),
    path("checkout/<str:tipo>", views.checkout, name="checkout"),
]
