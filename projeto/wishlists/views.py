from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import WishlistForm, ItemForm
from django.forms import modelformset_factory

from .models import Item


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

            return redirect('wishlist_list')
    else:
        form = WishlistForm()
        formset = ItemFormSet(queryset=Item.objects.none())

    return render(request, 'wishlists/criacao_wishlist.html', {'form': form, 'formset': formset})