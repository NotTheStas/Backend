from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product

def get_all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = [
            {"id": product.id, "name": product.name, "description": product.description}
            for product in products
        ]
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
def get_product_by_id(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=product_id)
        data = {"id": product.id, "name": product.name, "description": product.description}
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name and description:
            Product.objects.create(name=name, description=description)
            return redirect('/products/create')
        return render(request, 'mainapp/add_product.html')

    return render(request, 'mainapp/add_product.html')