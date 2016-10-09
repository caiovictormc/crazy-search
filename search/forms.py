from django import forms

from selectable.forms import AutoCompleteWidget

from .lookups import MyModelLookup


class MyModelForm(forms.Form):
    autocomplete = forms.CharField(
        label='Type the name of a model (AutoCompleteWidget)',
        widget=AutoCompleteWidget(MyModelLookup),
        required=False,
    )
