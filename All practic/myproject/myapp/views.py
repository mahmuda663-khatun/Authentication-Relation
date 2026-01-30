from django.shortcuts import render, redirect
from myapp.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash 
# Create your views here.

def home(r):
    return render (r,'home.html')

def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        Role=r.POST.get('Role')
        password=r.POST.get('password')
        email=r.POST.get('email')
        confirm_password=r.POST.get('confirm_password')

        user_exit=UserModel.objects.filter(username=username).exists()

        if user_exit:
            messages.warning(r,'user already exit')
            return redirect('signup')

        if confirm_password==password:
              UserModel.objects.create_user(
                username=username,
                Role=Role,
                password=confirm_password,
                email=email,
              )
              return redirect ('signin')

    return render (r,'signup.html')

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')

        user=authenticate(r,username=username,password=password)

        if user:
            login (r,user)
            messages.success(r,'successfully login')
            return redirect('home')
        else:
            messages.warning(r,'invalid')
            return redirect('signin')
    return render (r,'signin.html')

def signout(r):
    logout(r)
    return redirect ('signin')

def chengepass(r):
    current_user=r.user

    if r.method=="POST":
        current_password=r.POST.get('current_password')
        new_password=r.POST.get('new_password')
        confirm_password=r.POST.get('confirm_password')

        if check_password(current_password,current_user.password):

            if new_password==confirm_password:
                current_user.set_password('new_password')
                current_user.save()
                update_session_auth_hash(r,current_user)
                return redirect('home')

    return render (r,'chengepass.html')

def dep_page(r):
    d_data=
    return render (r,'dep_page.html')

def dep_edit(r,id):
    return render (r,'dep_edit.html')
    
def dep_delete(r,id):
    return redirect ('dep_page')

def studentpage(r):
    return render (r,'studentpage.html')

def studentEdit(r,id):
    return render (r,'studentEdit.html')

def studentDelete(r,id):
    return redirect ('studentpage')

