from django.shortcuts import render ,redirect
from myapp.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
# Create your views here.

@login_required
def home(r):
    all_data=RecipeModel.objects.all()
    context={
        'all_data':all_data
    }
    return render(r,'home.html',context)

def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        role=r.POST.get('role')
        email=r.POST.get('email')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')

        exits=UserModel.objects.filter(username=username).exists()

        if exits:
            messages.warning(r,'username already exit')
            return redirect('signup')

        if confirm_password==password:
            UserModel.objects.create_user(
                username=username,
                role=role,
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

        if user:
            login(r,user)
            messages.success(r,'successfully login')
            return redirect('home')
        else:
            messages.warning(r,'invalid')
            return redirect('signin')
    return render(r,'signin.html')

def signout(r):
    logout(r)
    return redirect('signin')

@login_required
def chengepass(r):
    current_user=r.user
    if r.method=="POST":
        current_password=r.POST.get('current_password')
        new_password=r.POST.get('new_password')
        Confirm_password=r.POST.get('Confirm_password')
        print(current_password,new_password,Confirm_password)

        if check_password(current_password,current_user.password):

            if new_password==Confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(r,current_user)
                return redirect('home')
    return render(r,'chengepass.html')

@login_required
def cate_page(r):
    d_data=CategoryModel.objects.all()
    if r.method=="POST":
        name=r.POST.get('name')
        description=r.POST.get('description')
        print(name,description)

        CategoryModel.objects.create(
            name=name,
            description=description,
        )
    context={
        'data':d_data
    }
    return render (r,'cate_page.html',context)


def cate_edit(r,id):
    E_data=CategoryModel.objects.get(id=id)
    if r.method=="POST":
        name=r.POST.get('name')
        description=r.POST.get('description')

        E_data.name=name
        E_data.description=description
        E_data.save()
        return redirect('cate_page')
    context={
        'E_data':E_data
    }
    return render (r,'cate_edit.html',context)

def cate_delete(r,id):
    CategoryModel.objects.get(id=id).delete()
    return redirect('cate_page')

@login_required
def recipe_page(r):
    r_data=RecipeModel.objects.filter(created_by=r.user)
    c_data=CategoryModel.objects.all()

    if r.method=="POST":
        title=r.POST.get('title')
        description=r.POST.get('description')
        ingredients=r.POST.get('ingredients')
        instructions=r.POST.get('instructions')
        image=r.FILES.get('image')
        category=r.POST.get('category')

        cate_data=CategoryModel.objects.get(id=category)

        RecipeModel.objects.create(
            title=title,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            image=image,
            category=cate_data,
            created_by=r.user,
        )
    context={
        'r_data':r_data,
        'c_data':c_data,
    }
    return render (r,'recipe_page.html',context)

def recipe_edit(r,id):
    return render (r,'recipe_edit.html')

def recipe_delete(r,id):
    return redirect('recipe_page')

