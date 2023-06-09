# Generated by Django 4.1.6 on 2023-06-09 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimAgroAssurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('OffreuAssurance', models.CharField(max_length=300)),
                ('TypeAssurance', models.CharField(max_length=300)),
                ('NbrSouscript', models.IntegerField()),
                ('CulturAssure', models.CharField(max_length=300)),
                ('NivPrime', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date_en', models.DateField(default=django.utils.timezone.now)),
                ('date_modification', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DimAgroCommercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('TypeVente', models.CharField(max_length=300)),
                ('ProdVenteSpecul', models.CharField(max_length=300)),
                ('PrixVentMoySaison', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ModEcoulement', models.CharField(max_length=300)),
                ('MarchRegroupement', models.CharField(max_length=300)),
                ('ClientAgro', models.CharField(max_length=300)),
                ('date_en', models.DateField(default=django.utils.timezone.now)),
                ('date_modification', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DimAgroCulture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('ZonProd_Cult', models.CharField(max_length=300)),
                ('Cultur_Pratique', models.CharField(max_length=300)),
                ('Type_Semence', models.CharField(max_length=300)),
                ('Codeculture', models.IntegerField()),
                ('Type_Culture_Pratique', models.CharField(max_length=250)),
                ('VarieteCultive', models.CharField(max_length=250)),
                ('SourcApprovisIntran', models.CharField(max_length=300)),
                ('SourcApprovisSemenc', models.CharField(max_length=300)),
                ('SourcApprovisEngrProdPhyto', models.CharField(max_length=300)),
                ('SourcApprovisMatAgro', models.CharField(max_length=300)),
                ('TypeAcquisIntran', models.CharField(max_length=300)),
                ('TypeAcquisMat', models.CharField(max_length=300)),
                ('TypeFertilisUtil', models.CharField(max_length=300)),
                ('TypePesticidUtil', models.CharField(max_length=300)),
                ('SupMoyDetenuMenag', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ModAcquisParcel', models.CharField(max_length=300)),
                ('date_en', models.DateField(default=django.utils.timezone.now)),
                ('date_modification', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DimAgroFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('OffreServicFinance', models.CharField(max_length=300)),
                ('DemandApport', models.CharField(max_length=250)),
                ('TypeGaranExige', models.CharField(max_length=300)),
                ('LongProcedCredi', models.CharField(max_length=300)),
                ('MontMoyTypeCultur', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TauxInteret', models.DecimalField(decimal_places=5, max_digits=10)),
                ('DelaiRembourse', models.CharField(max_length=300)),
                ('date_en', models.DateField(default=django.utils.timezone.now)),
                ('date_modification', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DimAgroOrganisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('TypeServicOfferOP', models.CharField(max_length=300)),
                ('BesoinForm', models.CharField(max_length=300)),
                ('ContrainGlobalAgro', models.CharField(max_length=300)),
                ('ContrainMajFilier', models.CharField(max_length=300)),
                ('InfrasStockCondition', models.CharField(max_length=300)),
                ('FournisEmballag', models.CharField(max_length=300)),
                ('date_en', models.DateField(default=django.utils.timezone.now)),
                ('date_modification', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DimAgroProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('CodeCulture', models.IntegerField()),
                ('SupMaxDetenu', models.DecimalField(decimal_places=5, max_digits=10)),
                ('SupMinDetenu', models.DecimalField(decimal_places=5, max_digits=10)),
                ('SupMoyDetenu', models.DecimalField(decimal_places=5, max_digits=10)),
                ('SupMoyEmblave', models.DecimalField(decimal_places=5, max_digits=10)),
                ('type_cult_prat', models.CharField(max_length=300)),
                ('RendemHectarCult', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TauxPertPostRecoltParCult', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TypeSolExist', models.CharField(max_length=300)),
                ('TypeDegradZonCultur', models.CharField(max_length=300)),
                ('CauseDegrad', models.CharField(max_length=300)),
                ('date_en', models.DateField(default=django.utils.timezone.now)),
                ('date_modification', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Visiteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('date_visiteur', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
