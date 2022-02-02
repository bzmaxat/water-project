from django.shortcuts import render
from .models import Catalog
from .models import Customer


def home(request):
    catalogs = Catalog.objects.all()
    return render(request, 'catalog/home.html', {'catalogs': catalogs})


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'catalog/customers.html', {'customers': customers})


def analysis(request):
    return render(request, 'catalog/analysis.html')


def branches(request):
    return render(request, 'catalog/branches.html')
