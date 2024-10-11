from django.shortcuts import render, redirect

from .forms import ListaForm, ItemFormSet
from .models import Lista, Item, Site, TipoWishlist


def homeview(request):
    return render(request, 'wishlist/home.html')

def criar_site(request):
    if request.method == 'POST':
        lista_form = ListaForm(request.POST)

        print(request.path)

        if lista_form.is_valid():
            if 'nome' in request.POST:

                tipo = request.path.split('/')[2]
                print("TIPO: ", tipo)

                tipo_wish = TipoWishlist.objects.get(
                    nome=tipo.title()
                )

                nome = request.POST.get('nome')
                lista = Lista.objects.create(nome=nome)
                site = Site.objects.create(nome=nome, url=nome, slug=nome, comprador=request.user, lista=lista)
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

            return redirect('base')

    else:
        lista_form = ListaForm()

    item_formset = ItemFormSet(queryset=Item.objects.none())

    return render(request, 'wishlist/criar_site.html', {
        'lista_form': lista_form,
        'item_formset': item_formset,
    })

def base(request):
    return render(request, 'wishlist/base.html')