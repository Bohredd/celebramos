from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ListaForm, ItemFormSet
from .models import Lista, Item, Site, TipoWishlist
from django.contrib.auth.decorators import login_required
import base64
import qrcode
from io import BytesIO
from django.http import HttpResponse


def homeview(request):
    return render(request, 'wishlist/home.html')

def tipos_wishlist(request):

    return render(request, 'wishlist/tipos_wishlist.html')

@login_required
def criar_site(request, tipo):
    if request.method == 'POST':
        lista_form = ListaForm(request.POST)

        print(request.path)

        if lista_form.is_valid():
            if 'nome' in request.POST:
                tipo_wish = TipoWishlist.objects.get(
                    nome=tipo.title()
                )

                nome = request.POST.get('nome')
                lista = Lista.objects.create(nome=nome)
                site = Site.objects.create(nome=nome, url=nome, comprador=request.user, lista_ativa=lista,
                                           tipo=tipo_wish)
                site.listas.add(lista)
                site.save()

            item_formset = ItemFormSet(request.POST)

            if item_formset.is_valid():
                quantia_itens = request.POST.get('form-TOTAL_FORMS')

                for item in range(0, int(quantia_itens) + 1):
                    item_nome = request.POST.get(f'form-{item}-nome')
                    item_descricao = request.POST.get(f'form-{item}-descricao')
                    item_site = request.POST.get(f'form-{item}-site')

                    if item_nome:
                        item = Item.objects.create(
                            nome=item_nome,
                            descricao=item_descricao,
                            site=item_site,
                        )

                        lista.itens.add(item)
                        lista.save()

            return redirect('checkout', tipo=tipo)

    else:
        lista_form = ListaForm()

    item_formset = ItemFormSet(queryset=Item.objects.none())

    return render(request, 'wishlist/criar_site.html', {
        'lista_form': lista_form,
        'item_formset': item_formset,
    })


def base(request):
    return render(request, 'wishlist/base.html')


def checkout(request, tipo):
    print("Tipo passado: ", tipo)

    tipo_wish = TipoWishlist.objects.get(
        nome=tipo.title()
    )

    return render(request, 'wishlist/checkout.html', {
        'tipo': tipo_wish
    })


def gerar_qr_code_compartilhamento(request, lista_id):
    url = request.build_absolute_uri(reverse('ver_lista', args=[lista_id]))

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    context = {
        'qr_code_image': img_str,
        'url': url
    }
    return render(request, 'wishlist/qr_code_compartilhamento.html', context)


def ver_lista(request, lista_id):
    lista = Lista.objects.get(id=lista_id)

    return render(request, 'wishlist/ver_lista.html', {
        'lista': lista

    })

@login_required
def minhas_wishlists(request):

    listas = Lista.objects.filter(site__comprador=request.user, site__ativo=True)

    return render(request, 'wishlist/minhas_wishlists.html', {
        'listas': listas
    })

@login_required
def wishlist_detalhes(request, lista_id):
    lista = Lista.objects.get(id=lista_id)

    return render(request, 'wishlist/wishlist_detalhes.html', {
        'lista': lista
    })