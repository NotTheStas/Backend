from django.urls import path
from .views import *

urlpatterns = [
    path('', test_request, name='test_request'),
]