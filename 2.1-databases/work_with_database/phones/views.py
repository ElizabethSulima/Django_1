from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

def catalog(request):
    phones = Phone.objects.all()
    # phones = Phone.objects.all().order_by('name')
    return render(request, 'catalog.html', {'phones': phones})

def phone_detail_view(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})
