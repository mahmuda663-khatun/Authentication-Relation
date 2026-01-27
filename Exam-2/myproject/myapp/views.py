from django.shortcuts import render,redirect
from myapp.models import*
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@login_required
def home(r):
    return render(r,'home.html')

def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        user_type=r.POST.get('user_type')
        email=r.POST.get('email')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')

        if confirm_password==password:
            UserModel.objects.create_user(
            username=username,
            user_type=user_type,
            email=email,
            password=password,
            )
            return redirect ('signin')
    return render (r,'signup.html')

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')

        user=authenticate(r,username=username,password=password)
        if user:
            login(r,user)
        return redirect('home') 
    return render(r,'signin.html')

def signout(r):
    logout(r)
    return redirect('signin')

def dep_list(r):
    d_data=DepartmentModel.objects.all()

    context={
        'data':d_data
    }
    return render(r,'deplist.html',context)

def dep_add(r):
        if r.method=="POST":
            departname=r.POST.get('departname')
            description=r.POST.get('description')

            DepartmentModel.objects.create(
                departname=departname,
                description=description,
            )
            return redirect("dep_list")
        return render(r,'depadd.html')

def dep_edit(r,id):
    E_data=DepartmentModel.objects.get(id=id)
    if r.method=="POST":
        departname=r.POST.get('departname')
        description=r.POST.get('description')

        E_data.departname=departname
        E_data.description=description
        E_data.save()
        return redirect('dep_list')
    context={
        'data':E_data
    }
    return render(r,'depedit.html',context)

def dep_delete(r,id):
    DepartmentModel.objects.get(id=id).delete()
    return redirect('dep_list')

def changepass(r):
    current_user=r.user
    if r.method=="POST":
        Current_password=r.POST.get('Current_password')
        new_password=r.POST.get('new_password')
        confirm_password=r.POST.get('confirm_password')

        if check_password(Current_password,current_user.password):

            if new_password==confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(r,current_user)
                return redirect ('home')
    return render(r,'chengepass.html')