from django.shortcuts import render, redirect
from myapp.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from decimal import Decimal 
# Create your views here.

@login_required
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
    d_data=DepartModel.objects.all()
    if r.method=="POST":
        name=r.POST.get('name')
        description=r.POST.get('description')

        DepartModel.objects.create(
            name=name,
            description=description,
        )

    context={
        'data':d_data
    }
    return render (r,'dep_page.html',context)

def dep_edit(r,id):
    d_data=DepartModel.objects.get(id=id)
    if r.method=="POST":
        name=r.POST.get('name')
        description=r.POST.get('description')

        d_data.name=name
        d_data.description=description
        d_data.save()
        return redirect(dep_page)
    context={
        'data':d_data
    }
    return render (r,'dep_edit.html',context)
    
def dep_delete(r,id):
    DepartModel.objects.get(id=id).delete()
    return redirect ('dep_page')

def studentpage(r):
    s_data=StudentModel.objects.all()
    d_data=DepartModel.objects.all()
    if r.method=="POST":
        name=r.POST.get('name')
        image=r.FILES.get('image')
        department=r.POST.get('department')
        food_per=Decimal(r.POST.get('food_per'))
        food_fee=Decimal(r.POST.get('food_fee'))

        total_fee=(food_fee*food_per/100)

        user=DepartModel.objects.get(id=department)

        StudentModel.objects.create(
            name=name,
            image=image,
            department=user,
            food_per=food_per,
            total_fee=total_fee,
            food_fee=food_fee,
        )
        
    context={
        'data':s_data,
        'd_data':d_data
    }
    return render (r,'studentpage.html',context)

def studentEdit(r,id):
    return render (r,'studentEdit.html')

def studentDelete(r,id):
    return redirect ('studentpage')

