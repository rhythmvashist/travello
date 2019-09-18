from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import  messages

# Create your views here.

def register(request):
    if request.method == 'POST' :
        first=request.POST['first_name']
        last=request.POST['last_name']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        email=request.POST['email']
        username=request.POST['username']

        if pass1 ==pass2:
            if User.objects.filter(username=username).exists():
               messages.info (request,'user name taken')
               return redirect('register')
            elif  User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=pass1,email=email,first_name=first,last_name=last)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html',)


def login(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=user,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')