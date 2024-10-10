from django import forms
from .models import Lista, Item
from django.forms import modelformset_factory

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['nome']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'descricao', 'site']

ItemFormSet = modelformset_factory(Item, form=ItemForm, extra=0)
