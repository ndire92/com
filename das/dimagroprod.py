from django.forms import ModelForm
from das.models import DimAgroProduction
from django import forms


class DimAgroprd(ModelForm):

    codeCommune= forms.CharField(label='Code Commune',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(label='Nom Commune',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    CodeCulture = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SupMaxDetenu = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SupMinDetenu = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SupMoyDetenu = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SupMoyEmblave= forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    type_cult_prat = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    RendemHectarCult = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TauxPertPostRecoltParCult = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeSolExist = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeDegradZonCultur = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    CauseDegrad = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date_en=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;', 'class': 'form-control'}))
    date_modification=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;', 'class': 'form-control'}))
    

    class Meta:
        model = DimAgroProduction
        fields = ['codeCommune','nomCommune','CodeCulture', 'SupMaxDetenu','SupMinDetenu','SupMoyDetenu','SupMoyEmblave','type_cult_prat', 'RendemHectarCult',
                  'TauxPertPostRecoltParCult', 'TypeSolExist', 'TypeDegradZonCultur', 'CauseDegrad','date_en','date_modification']
