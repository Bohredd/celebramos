import base64
import io

import qrcode
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import WishlistForm, ItemForm, EscolherPlanoForm
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Item, PlanoCredito, Wishlist
from django.utils.safestring import mark_safe

from usuarios.models import Usuario
from decouple import config


def pagina_inicial(request):
    return render(request, 'wishlists/pagina_inicial.html')


@login_required
def criacao_wishlist(request):
    ItemFormSet = modelformset_factory(Item, form=ItemForm, extra=1, can_delete=True)

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        formset = ItemFormSet(request.POST, queryset=Item.objects.none())

        if form.is_valid() and formset.is_valid():
            wishlist = form.save(commit=False)
            wishlist.comprado_por = request.user
            wishlist.save()

            itens = formset.save(commit=False)
            for item in itens:
                item.save()

            wishlist.itens.set(itens)
            wishlist.save()

            if wishlist.creditos_colocados > request.user.creditos:
                wishlist.delete()
                messages.error(request,
                               f'Você não possui créditos suficientes para criar essa wishlist. Créditos disponíveis: {request.user.creditos}.')

                url_creditos = reverse('comprar_creditos')

                messages.info(request, mark_safe(
                    f"Caso queira adicionar mais créditos, clique <a href='{url_creditos}'>aqui</a>."))
            else:
                wishlist.foi_paga = True
                wishlist.valida = True
                wishlist.save()
                request.user.creditos -= wishlist.creditos_colocados
                request.user.save()
                messages.success(request, 'Wishlist criada com sucesso!')
                return redirect('ver_wishlist', wishlist_id=wishlist.id)
    else:
        form = WishlistForm()
        formset = ItemFormSet(queryset=Item.objects.none())

    return render(request, 'wishlists/criacao_wishlist.html', {'form': form, 'formset': formset})


def comprar_creditos(request):
    planos = PlanoCredito.objects.all()

    if request.method == 'POST':
        form = EscolherPlanoForm(request.POST)
        if form.is_valid():
            plano_id = form.cleaned_data['plano_id']
            plano_selecionado = PlanoCredito.objects.get(id=plano_id)

            if request.user == Usuario.objects.get(
                    email=config("ADMIN_EMAIL")
            ):
                request.user.creditos += plano_selecionado.quantidade
                request.user.save()
                messages.success(request,
                                 f'Créditos adicionados com sucesso! Seu saldo atual é de {request.user.creditos}.')
            else:
                return redirect('checkout_pagamento', plano_id=plano_id)
        else:
            messages.error(request, 'Erro ao adicionar créditos.')
    else:
        form = EscolherPlanoForm()
    return render(request, 'wishlists/comprar_creditos.html', {'planos': planos, 'form': form})

def checkout_pagamento(request, plano_id):
    plano = PlanoCredito.objects.get(id=plano_id)
    return render(request, 'wishlists/checkout_pagamento.html', {'plano': plano})

def compartilhar_wishlist(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, id=wishlist_id)

    url_wishlist = request.build_absolute_uri(f'/ver/c/{wishlist_id}/')

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url_wishlist)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img.seek(0)

    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render(request, 'wishlists/compartilhar_wishlist.html', {
        'wishlist': wishlist,
        'qr_code': img_base64,
    })

def ver_wishlist_cliente(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id)
    itens = wishlist.itens.all()
    return render(request, 'wishlists/ver_wishlist.html', {'wishlist': wishlist, 'itens': itens})

def ver_wishlist_convidado(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id)
    itens = wishlist.itens.all()
    return render(request, 'wishlists/ver_wishlist.html', {'wishlist': wishlist, 'itens': itens})