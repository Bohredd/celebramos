from django.urls import path
from .views import cadastro_usuario, login_usuario, esqueci_senha
urlpatterns = [
    path('cadastro/', cadastro_usuario, name='cadastro_usuario'),
    path('login/', login_usuario, name='login_usuario'),
    path('esqueci-senha/', esqueci_senha, name='esqueci_senha'),
]
