
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeview, name='home'),
    path('criar_site/', views.criar_site, name='criar_site'),
    path('base/', views.base, name='base'),
]
