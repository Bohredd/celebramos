from django.shortcuts import render

from wishlist.forms import SiteForm


def homeview(request):
    return render(request, 'wishlist/home.html')

def criar_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        print(form.is_valid())
        print(form.cleaned_data)
        if form.is_valid():
            # Processar o formulário
            # form.cleaned_data['tipo'], form.cleaned_data['nome'] - dados disponíveis aqui
            # Salvar no banco de dados ou realizar outras ações necessárias
            pass
    else:
        form = SiteForm()

    return render(request, 'wishlist/criar_site.html', {'form': form})