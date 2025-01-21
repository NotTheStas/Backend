from django.urls import path
from .views import *

urlpatterns = [
    path('gateway/', redirect_mainapp, name='redirect_mainapp'),
]