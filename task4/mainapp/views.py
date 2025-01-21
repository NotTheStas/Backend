from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not password or not confirm_password:
            return redirect('register')

        if password != confirm_password:
            return redirect('register')

        if User.objects.filter(username=username).exists():
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'mainapp/register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            return redirect('login')

    return render(request, 'mainapp/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')