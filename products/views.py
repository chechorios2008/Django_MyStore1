from django.shortcuts import render

from .models import Product

def index(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'list_of_products.html', 
                  {'products': products})
    
def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'show_product.html',
                  {'product':product})
