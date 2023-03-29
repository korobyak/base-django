from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import ProductCategory, Product, Bucket


# Create your views here.
def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)

@login_required
def bucket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    buckets = Bucket.objects.filter(user=request.user, product=product)

    if not buckets.exists():
        Bucket.objects.create(user=request.user, product=product, quantity=1)
    else:
        bucket = buckets.first()
        bucket.quantity += 1
        bucket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def bucket_remove(request, bucket_id):
    bucket = Bucket.objects.get(id=bucket_id)
    bucket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])