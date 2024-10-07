from django import forms
from .models import Item, Lista, Site


class SiteForm(forms.Form):
    basico = forms.BooleanField(
        required=False,
        label="Site Básico",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        help_text="1 mês, 1 foto, sem música. R$19,99."
    )
    profissional = forms.BooleanField(
        required=False,
        label="Site Profissional",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        help_text="3 meses, 5 fotos, com música. R$39,99."
    )
    nome = forms.CharField(
        max_length=100,
        label="Nome da Ocasião",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    labels = {
        'basico': 'Site Básico',
        'profissional': 'Site Profissional',
        'nome': 'Nome da Ocasião'

    }

    def clean(self):
        cleaned_data = super().clean()
        basico = cleaned_data.get('basico')
        profissional = cleaned_data.get('profissional')

        # Se ambos forem selecionados, lançar um erro de validação
        if basico and profissional:
            raise forms.ValidationError("Você só pode selecionar uma opção: Site Básico ou Site Profissional.")

        # Se nenhum for selecionado, lançar um erro
        if not basico and not profissional:
            raise forms.ValidationError("Você precisa selecionar uma das opções: Site Básico ou Site Profissional.")

        return cleaned_data

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'descricao', 'site', 'comprado']
        widgets = {
            'comprado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'nome': 'Nome do Item',
            'descricao': 'Descrição do Item',
            'site': 'Site para Compra',
            'comprado': 'Comprado?'
        }


class ListaForm(forms.ModelForm):
    itens = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Lista
        fields = ['nome', 'itens']
        labels = {
            'nome': 'Nome da Lista',
            'itens': 'Itens da Lista'
        }
