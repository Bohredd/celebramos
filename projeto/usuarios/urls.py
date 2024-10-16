from django.urls import path
from .views import cadastro_usuario, login_usuario, esqueci_senha, minha_conta, ativar_conta
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', cadastro_usuario, name='cadastro_usuario'),
    path('login/', login_usuario, name='login_usuario'),
    path('esqueci-senha/', esqueci_senha, name='esqueci_senha'),
    path('minha-conta/', minha_conta, name='minha_conta'),
    path('ativar/<uidb64>/<token>/', ativar_conta, name='ativar_conta'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
