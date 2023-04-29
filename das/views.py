from django.shortcuts import render, redirect
from das.dimagroprod import DimAgroprd
from das.dimagrofi import DimAgrofinf
from das.dimaroassur import DimAgroAssurancef
from das.dimcom import AgroCommercial

from django.core.paginator import Paginator
from das.dimagroorg import DimAgroorg
from django.http import HttpResponseRedirect
from das.dimagrocul import DimAgrocultf
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib import messages


from das.models import DimAgroAssurance, DimAgroCommercial, DimAgroCulture, DimAgroFinance, DimAgroOrganisation, DimAgroProduction


# Create your views here.


def dimagr(request,):

    return render(request, 'page/Dimassu.html')


def agro_assu_form(request):

    if request.method == 'POST':
        form = DimAgroAssurancef(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")

            return redirect('/das/dimagroassu/')
    else:
        form = DimAgroAssurancef()
    return render(request, 'page/dimagroassur.html', {'form': form, 'dataObject': DimAgroAssurance.objects.all()})

# update


def update_a(request, id):
    dataObject = DimAgroAssurance.objects.get(id=id)
    form = DimAgroAssurancef(instance=dataObject)
    if request.method == 'POST':
        form = DimAgroAssurancef(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, ' succefully ')
            return redirect('/das/dimagroassu/')

    context = {

        'form': form,

    }
    return render(request, 'page/dimagroassur.html', context)


def delete_post(request, id):
    dataObject = DimAgroAssurance.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/das/dimagroassu/')
    context = {

        'item': dataObject, }
    return render(request, 'page/delete.html', context)


def dimagrocul_form(request):
    if request.method == 'POST':
        form = DimAgrocultf(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimagrocul/')
    else:
        form = DimAgrocultf()

    return render(request, 'page/dimagrocul.html', {'form': form, 'dataOb': DimAgroCulture.objects.all()})


# update agrocul
def update_c(request, id):
    dataObject = DimAgroCulture.objects.get(id=id)
    form = DimAgrocultf(instance=dataObject)
    if request.method == 'POST':
        form = DimAgrocultf(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimagrocul/')

    context = {

        'form': form,

    }
    return render(request, 'page/dimagrocul.html', context)


def delete_d(request, id):
    dataObject = DimAgroCulture.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/das/dimagrocul/')
    context = {

        'item': dataObject, }
    return render(request, 'page/delete_c.html', context)


def dimagrofin_form(request):
    if request.method == 'POST':
        form = DimAgrofinf(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimagrofin/')
    else:
        form = DimAgrofinf()

    return render(request, 'page/dimagrofin.html', {'form': form, 'dataObject': DimAgroFinance.objects.all()})


# update fina
def update_f(request, id):
    dataObject = DimAgroFinance.objects.get(id=id)
    form = DimAgrofinf(instance=dataObject)
    if request.method == 'POST':
        form = DimAgrofinf(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()

            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimagrofin/')

    context = {

        'form': form,

    }
    return render(request, 'page/dimagrofin.html', context)


def delete_f(request, id):
    dataObject = DimAgroFinance.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/das/dimagrofin/')
    context = {

        'item': dataObject, }
    return render(request, 'page/delete_fi.html', context)


def dimagroorg_form(request):
    if request.method == 'POST':
        form = DimAgroorg(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimagroog/')
    else:
        form = DimAgroorg()

    return render(request, 'page/dimagroorg.html', {'form': form, 'dataObject': DimAgroOrganisation.objects.all()})


# update agroorg
def update_or(request, id):
    dataObject = DimAgroOrganisation.objects.get(id=id)
    form = DimAgroorg(instance=dataObject)
    if request.method == 'POST':
        form = DimAgroorg(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()

            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimagroog/')

    context = {

        'form': form,

    }
    return render(request, 'page/dimagroorg.html', context)


def delete_or(request, id):
    dataObject = DimAgroOrganisation.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/das/dimagrofin/')
    context = {

        'item': dataObject, }
    return render(request, 'page/delete_org.html', context)


def dimagrprod_form(request):
    if request.method == 'POST':
        form = DimAgroprd(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimagroprod/')
    else:
        form = DimAgroprd()

    return render(request, 'page/dimagroprod.html', {'form': form, 'dataObject': DimAgroProduction.objects.all()})


# update prod
def update_prd(request, id):
    dataObject = DimAgroProduction.objects.get(id=id)
    form = DimAgroprd(instance=dataObject)
    if request.method == 'POST':
        form = DimAgroprd(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()

            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimagroprod/')

    context = {

        'form': form,

    }
    return render(request, 'page/dimagroprod.html', context)


def delete_prd(request, id):
    dataObject = DimAgroProduction.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/das/dimagroprod/')
    context = {

        'item': dataObject, }
    return render(request, 'page/delete_prd.html', context)


def AgroCm(request):
    if request.method == 'POST':
        form = AgroCommercial(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimcom/')
    else:
        form = AgroCommercial()

    return render(request, 'page/dimcom.html', {'form': form, 'dataObject': DimAgroCommercial.objects.all()})


# update prod

def update_com(request, id):
    dataObject = DimAgroCommercial.objects.get(id=id)
    form = AgroCommercial(instance=dataObject)
    if request.method == 'POST':
        form = AgroCommercial(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()

            messages.success(request, " Are Successfully Added !")
            return redirect('/das/dimcom/')

    context = {

        'form': form,

    }
    return render(request, 'page/dimcom.html', context)


def delete_com(request, id):
    dataObject = DimAgroCommercial.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/das/dimcom/')
    context = {

        'item': dataObject, }
    return render(request, 'page/delete_prd.html', context)
