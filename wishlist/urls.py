
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeview, name='home_pt'), # em portugues
    path('en/', views.homeview, name='home_en'), # em ingles
    path('cw/basico/', views.criar_site, name='wish_basica'),
    path('cw/profissional/', views.criar_site, name='wish_profissional'),
    path('base/', views.base, name='base'),
]
