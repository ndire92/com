from django.db import models
from django.utils import timezone

# Create your models here.
class DimAgroAssurance(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    OffreuAssurance = models.CharField(max_length=300)
    TypeAssurance = models.CharField(max_length=300)
    NbrSouscript = models.IntegerField()
    CulturAssure = models.CharField(max_length=300)
    NivPrime = models.DecimalField(max_digits=10,decimal_places=5)
    date_en =models.DateField(default=timezone.now)
    date_modification = models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return self.OffreuAssurancel
    
class DimAgroCulture (models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)

    ZonProd_Cult = models.CharField(max_length=300)
    Cultur_Pratique = models.CharField(max_length=300)
    Type_Semence = models.CharField(max_length=300)
    Codeculture =models.IntegerField()
    Type_Culture_Pratique = models.CharField(max_length=250)
    VarieteCultive = models.CharField(max_length=250)
    SourcApprovisIntran = models.CharField(max_length=300)
    SourcApprovisSemenc = models.CharField(max_length=300)
    SourcApprovisEngrProdPhyto = models.CharField(max_length=300)
    SourcApprovisMatAgro = models.CharField(max_length=300)
    TypeAcquisIntran = models.CharField(max_length=300)
    TypeAcquisMat = models.CharField(max_length=300)
    TypeFertilisUtil = models.CharField(max_length=300)
    TypePesticidUtil = models.CharField(max_length=300)
    SupMoyDetenuMenag= models.DecimalField(max_digits=10,decimal_places=5)
    ModAcquisParcel = models.CharField(max_length=300)
    date_en =models.DateField(default=timezone.now)
    date_modification = models.DateField(default=timezone.now)

    def __str__(self):

        return self.ZonProd_Cult


class DimAgroFinance(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)

    OffreServicFinance = models.CharField(max_length=300)
    DemandApport = models.CharField(max_length=250)
    TypeGaranExige = models.CharField(max_length=300)
    LongProcedCredi = models.CharField(max_length=300)
    MontMoyTypeCultur = models.DecimalField(max_digits=10,decimal_places=5)
    TauxInteret = models.DecimalField(max_digits=10,decimal_places=5)
    DelaiRembourse = models.CharField(max_length=300)
    date_en =models.DateField(default=timezone.now)
    date_modification = models.DateField(default=timezone.now)

    def __str__(self):
        return self.OffreServicFinance


class DimAgroOrganisation(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    
    TypeServicOfferOP = models.CharField(max_length=300)
    BesoinForm = models.CharField(max_length=300)
    ContrainGlobalAgro = models.CharField(max_length=300)
    ContrainMajFilier = models.CharField(max_length=300)
    InfrasStockCondition = models.CharField(max_length=300)
    FournisEmballag = models.CharField(max_length=300)
    date_en =models.DateField(default=timezone.now)
    date_modification = models.DateField(default=timezone.now)
    

    def __str__(self):
        return self.nomCommune

    




class DimAgroProduction(models.Model):

    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    CodeCulture = models.IntegerField()
    SupMaxDetenu =  models.DecimalField(max_digits=10,decimal_places=5)
    SupMinDetenu =  models.DecimalField(max_digits=10,decimal_places=5)
    SupMoyDetenu =  models.DecimalField(max_digits=10,decimal_places=5)
    SupMoyEmblave=  models.DecimalField(max_digits=10,decimal_places=5)
    type_cult_prat= models.CharField(max_length=300)
    RendemHectarCult  = models.DecimalField(max_digits=10,decimal_places=5)
    TauxPertPostRecoltParCult  = models.DecimalField(max_digits=10,decimal_places=5)
    TypeSolExist  = models.CharField(max_length=300)
    TypeDegradZonCultur  = models.CharField(max_length=300)
    CauseDegrad  = models.CharField(max_length=300)

    date_en =models.DateField(default=timezone.now)
    date_modification = models.DateField(default=timezone.now)
    

    def __str__(self):
        return self.nomCommune

    
class DimAgroCommercial(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    TypeVente  =models.CharField(max_length=300)
    ProdVenteSpecul = models.CharField(max_length=300)
    PrixVentMoySaison= models.DecimalField(max_digits=10,decimal_places=5)
    ModEcoulement  =models.CharField(max_length=300)
    MarchRegroupement =models.CharField(max_length=300)
    ClientAgro  =models.CharField(max_length=300)
    date_en =models.DateField(default=timezone.now)
    date_modification = models.DateField(default=timezone.now)

    
    def __str__(self):
        return self.nomCommune
    
class Visiteur (models.Model):
    nom = models.CharField(max_length=25)
    date_visiteur = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
