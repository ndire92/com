from django.forms import ModelForm
from das.models import DimAgroOrganisation
from django import forms


class DimAgroorg(ModelForm):
    codeCommune= forms.CharField(label='Code Commune',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(label='nom Commune',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))

    TypeServicOfferOP = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    BesoinForm = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    ContrainGlobalAgro = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ContrainMajFilier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    InfrasStockCondition = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    FournisEmballag = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date_en=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;', 'class': 'form-control'}))
    date_modification=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;', 'class': 'form-control'}))
    

    class Meta:
        model = DimAgroOrganisation
        fields = ['codeCommune','nomCommune', 'TypeServicOfferOP', 'BesoinForm',
                  'ContrainGlobalAgro', 'ContrainMajFilier', 'InfrasStockCondition', 'FournisEmballag','date_en','date_modification']
