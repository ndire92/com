from django.forms import ModelForm
from das.models import DimAgroCulture
from django import forms


class DimAgrocultf(ModelForm):
    codeCommune= forms.CharField(label='Code Commune',widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(label='Code Commune',widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    ZonProd_Cult  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Cultur_Pratique  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Type_Semence  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Codeculture  = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    Type_Culture_Pratique = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    VarieteCultive = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovisIntran  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovisSemenc  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovisEngrProdPhyto  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SourcApprovisMatAgro  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeAcquisIntran  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeAcquisMat  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypeFertilisUtil  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    TypePesticidUtil  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SupMoyDetenuMenag= forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    ModAcquisParcel  = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))  
    date_en=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;', 'class': 'form-control'}))
    date_modification=  forms.CharField(widget=forms.DateInput(attrs={'type': 'date','style': 'width: 300px;', 'class': 'form-control'}))
    

    class Meta:
        model = DimAgroCulture
        fields = ['codeCommune','nomCommune','ZonProd_Cult', 'Cultur_Pratique', 'Type_Semence','Codeculture' ,'Type_Culture_Pratique', 'VarieteCultive', 'SourcApprovisIntran', 'SourcApprovisSemenc',
                  'SourcApprovisEngrProdPhyto', 'SourcApprovisMatAgro', 'TypeAcquisIntran', 'TypeAcquisMat', 'TypeFertilisUtil', 'TypePesticidUtil','SupMoyDetenuMenag','ModAcquisParcel','date_en','date_modification']
