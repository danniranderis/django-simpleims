from django import forms
from dal import autocomplete
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'tags': autocomplete.ModelSelect2Multiple(
                url='ims:tag-autocomplete'),
        }
