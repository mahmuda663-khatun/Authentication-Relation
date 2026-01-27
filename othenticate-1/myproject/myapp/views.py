from django.shortcuts import render,redirect
from myapp.models import*
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(r):
    return render(r,'home.html')

def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        email=r.POST.get('email')
        Role=r.POST.get('Role')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')

        if confirm_password==password:
            UserModel.objects.create_user(
            username=username,
            email=email,
            Role=Role,
            password=password,
        )
        return redirect('signin')
    return render(r,'signup.html')

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')

        user=authenticate(r,username=username,password=password)

        if user:
            login (r,user)
            return redirect('home')
    return render (r,'signin.html')

def signout(r):
    logout(r)
    return redirect('signin')


        