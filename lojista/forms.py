from django import forms
from tempus_dominus.widgets import DatePicker

from produtos.models import Produto


class CriarProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "name",
            "price",
            "qnt_stock",
            "sold",
            "category",
            "description",
            "image",
            'expiration_date',
        ]
        widgets = {'expiration_date': DatePicker(
            options={
                'minDate': '2022-05-20',
            }
        )}
