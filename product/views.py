from django.http import HttpResponse
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


def category(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    products = Product.objects.filter(category_id=id)
    categories = Category.objects.all()
    return render(request, "home.html", {"products": products,
                                         'cart': len(request.session['carrinho']),
                                         'categories': categories
                                         })


def product(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    error = request.GET.get('error')
    product = Product.objects.filter(id=id)[0]
    categories = Category.objects.all()
    return render(request, "product.html", {"product": product,
                                            'cart': len(request.session['carrinho']),
                                            'categories': categories,
                                            'error': error
                                            })
