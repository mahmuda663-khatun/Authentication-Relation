from django.shortcuts import render,redirect
from myapp.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
# Create your views here.
@login_required
def home(r):
    return render (r,'home.html')

def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        user_type=r.POST.get('user_type')
        email=r.POST.get('email')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')

        if confirm_password==password:
           AuthenticateModel.objects.create_user(
              username=username, 
              user_type=user_type, 
              email=email,
              password=password, 
           )
           return redirect('signin') 
    return render(r,'signup.html')

def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')

        user=authenticate(r,username=username,password=password)
        username=username, 
        password=password,
        if user:
            login(r,user)
            messages.success(r,'successfully login')
            return redirect ('home')
    return render(r,'signin.html')

def signout(r):
    logout(r)
    return redirect('signin')

def dep_list(r):
    d_data=DepartmentModel.objects.all()
    context={
        'data':d_data
    }
    return render(r,'dep_list.html',context)

def dep_add(r):
    if r.method=="POST":
        dep_name=r.POST.get('dep_name')
        description=r.POST.get('description')

        DepartmentModel.objects.create(
            dep_name=dep_name,
            description=description,
        )
        return redirect('dep_list')
    return render(r,'dep_add.html')

def dep_edit(r,id):
    d_data=DepartmentModel.objects.get(id=id)
    if r.method=="POST":
        dep_name=r.POST.get('dep_name')
        description=r.POST.get('description')

        d_data.dep_name=dep_name
        d_data.description=description
        d_data.save()
        return redirect('dep_list')
    context={
        'data':d_data
    }
    return render(r,'dep_edit.html',context)

def dep_delete(r,id):
    DepartmentModel.objects.get(id=id).delete()
    return redirect('dep_list')

def employeelist(r):
    e_data=EmployeeModel.objects.all()
    context={
        'data':e_data
    }
    return render(r,'employeelist.html',context)

def employeeAdd(r):
    e_data=DepartmentModel.objects.all()
    if r.method=="POST":
        name=r.POST.get('name')
        designation=r.POST.get('designation')
        Address=r.POST.get('Address')
        image=r.FILES.get('image')
        department=r.POST.get('department')

        dep=DepartmentModel.objects.get(id=department)

        EmployeeModel.objects.create(
            name=name,
            designation=designation,
            Address=Address,
            image=image,
            department=dep,
        )
        return redirect('employeelist')
    contxt={
        'dept':e_data
    }
    return render(r,'employeeAdd.html',contxt)
