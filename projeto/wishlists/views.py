from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import WishlistForm, ItemForm, EscolherPlanoForm
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Item, PlanoCredito
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
                item.wishlist = wishlist
                item.save()

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
                return redirect('wishlist_list')
    else:
        form = WishlistForm()
        formset = ItemFormSet(queryset=Item.objects.none())

    return render(request, 'wishlists/criacao_wishlist.html', {'form': form, 'formset': formset})


def comprar_creditos(request):
    planos = PlanoCredito.objects.all()  # Obter todos os planos

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
