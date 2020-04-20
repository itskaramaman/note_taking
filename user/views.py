from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check']

        if password != password_check:
            return redirect('register')

        if User.objects.filter(username=username).exists():
            return redirect('register')

        if User.objects.filter(email=email).exists():
            return redirect('register')

        user = User.objects.create_user(username=username, email=email,
                                        password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('login')
    return render(request, 'user/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if not user:
            return redirect('login')
        auth.login(request, user)
        return redirect('home')
    return render(request, 'user/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
