from dal import autocomplete
from django import forms
from search.models import MyModel



class MyModelForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=MyModel.objects.all(),
        widget=autocomplete.ModelSelect2(
                    url='search:model-autocomplete',
                    attrs={
                        'data-placeholder': 'Name of Model',
                        'data-minimum-input-length': 3,
                    })
    )

    class Meta:
        model = MyModel
        fields = ('name', )


'''
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('__all__')
        widgets = {
            'name': autocomplete.ModelSelect2(url='model-autocomplete')
        }
'''
