from django.urls import path
from .views import *

urlpatterns = [
    path('', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout, name='logout'),
]