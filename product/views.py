from django.shortcuts import render
from .models import Product, Category, Options, Additional


def home(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "home.html", {"products": products,
                                         'cart': len(request.session['carrinho']),
                                         'categories': categories
                                         })


def category(request):
    pass
