
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# from django.template import engine
# from django.template import Engine, EngineHandler, engines

from django.contrib import messages


from das.models import DimAgroAssurance, DimAgroCommercial, DimAgroCulture, DimAgroFinance, DimAgroOrganisation, DimAgroProduction, Visiteur


# @login_required(login_url='/')
def Home(request):
    dataassu = DimAgroAssurance.objects.all().count()
    datacom = DimAgroCommercial.objects.all().count()
    datacul = DimAgroCulture.objects.all().count()
    datafin = DimAgroFinance.objects.all().count()
    dataorg = DimAgroOrganisation.objects.all().count()
    dataprod = DimAgroProduction.objects.all().count()
    nb_visite = Visiteur.objects.all().count()

    context = {
        'dataassu': dataassu,
        'datacom': datacom,
        'datacul': datacul,
        'datafin': datafin,
        'dataorg': dataorg,
        'dataprod': dataprod,
        'nb_visite': nb_visite,
    }
    return render(request, 'Hod/home.html', context)
