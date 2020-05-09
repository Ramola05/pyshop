from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# like when you edit some files
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('New  products will display here')


# use vs code instead of pycharmß

#after editing a file or mutiples just save them and do what im gonna do next


