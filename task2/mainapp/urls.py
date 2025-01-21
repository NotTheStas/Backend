from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_all_products, name='get_all_products'),  # API: список всех продуктов
    path('products/<int:product_id>/', views.get_product_by_id, name='get_product_by_id'),  # API: продукт по ID
    path('products/create/', views.create_product, name='add_product'),  # Страница и API для создания продукта
]