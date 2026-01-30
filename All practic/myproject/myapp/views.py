from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash 
# Create your views here.

def home(r):
    return render (r,'home.html')

def signup(r):
    return render (r,'signup.html')

def signin(r):
    return render (r,'signin.html')

def signout(r):
    return redirect ('signin')

def chengepass(r):
    return render (r,'chengepass.html')

def dep_page(r):
    return render (r,'department.html')

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

