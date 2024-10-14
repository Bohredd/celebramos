from django import forms

from .models import Wishlist, Item, PlanoCredito

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['nome_evento', 'descricao_evento', 'data_evento', 'horario_evento', 'link_musica', 'creditos_colocados']
        widgets = {
            'data_evento': forms.DateInput(attrs={'type': 'date'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome_item', 'link_compra',]

class EscolherPlanoForm(forms.Form):
    plano_id = forms.IntegerField(widget=forms.HiddenInput())