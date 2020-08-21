from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name,
                                                last_name=last_name, email=email, password=password1)
                user.save()
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
        return redirect('/')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']   
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
        return redirect('/')

    else:
        return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('register')