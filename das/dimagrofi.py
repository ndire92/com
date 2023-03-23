from django.forms import ModelForm
from das.models import DimAgroFinance
from django import forms


class DimAgrofinf(ModelForm):
    codeCommune= forms.CharField(label='Code Commune',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(label='Code Commune',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))

    OffreServicFinance = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DemandApport = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeGaranExige = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    LongProcedCredi = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    MontMoyTypeCultur = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TauxInteret  = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    DelaiRembourse = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    date_en=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 800px;', 'class': 'form-control'}))
    date_modification=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 800px;', 'class': 'form-control'}))
    

    class Meta:
        model = DimAgroFinance
        fields = ['codeCommune','nomCommune','OffreServicFinance', 'DemandApport',
                  'TypeGaranExige', 'LongProcedCredi','MontMoyTypeCultur','TauxInteret' ,'DelaiRembourse','date_en','date_modification']
