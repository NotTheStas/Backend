from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_page, name='products_page'),
]