from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import WishlistForm, ItemForm
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Item
from django.utils.safestring import mark_safe


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
                messages.error(request, f'Você não possui créditos suficientes para criar essa wishlist. Créditos disponíveis: {request.user.creditos}.')
                messages.info(request, mark_safe(
                    "Caso queira adicionar mais créditos, clique <a href='/usuarios/creditos'>aqui</a>."))
                return render(request, 'wishlists/criacao_wishlist.html', {'form': form, 'formset': formset})
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