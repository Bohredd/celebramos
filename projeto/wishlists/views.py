from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'wishlists/pagina_inicial.html')

@login_required
def criacao_wishlist(request):
    return render(request, 'wishlists/criacao_wishlist.html')