from django.shortcuts import redirect, render
from .models import Product


def products_page(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'mainapp/products.html', {'products': products})

    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if name and description:
            Product.objects.create(name=name, description=description)

        return redirect('products_page')