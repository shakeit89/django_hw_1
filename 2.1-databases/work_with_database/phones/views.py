from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    print(sort)

    phone_object = Phone.objects.all()
    if sort == "name":
        phone_object = phone_object.order_by('name')
    elif sort == "min_price":
        phone_object = phone_object.order_by('price')
    elif sort == "max_price":
        phone_object = phone_object.order_by('-price')

    context = {'phones': phone_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    print(phone_object)
    context = {'phone': phone_object}
    return render(request, template, context)
