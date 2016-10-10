from dal import autocomplete
from django import forms
from search.models import MyModel


class MyModelForm(forms.ModelForm):
    nasme = forms.CharField(max_length=200)
    model_name = forms.ModelChoiceField(
        queryset=MyModel.objects.all(),
        widget=autocomplete.ModelSelect2(url='/')
    )
    class Meta:
        model = MyModel
        fields = ('__all__')
