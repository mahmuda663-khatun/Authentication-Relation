from django.shortcuts import render,redirect
from product.models import*
# Create your views here.

def home(r):
    return render (r,'home.html')

def add_cate(r):
    if r.method=="POST":
        name=r.POST.get('name')

        CategoryModel.objects.create(
            name=name
        )
        return redirect('list_cate')
    return render(r,'add_cate.html')

def list_cate(r):
    c_data=CategoryModel.objects.all()
    context={
        'data':c_data
    }
    return render(r,'list_cate.html',context)

def edit_cate(r,id):
    data=CategoryModel.objects.get(id=id)
    if r.method=="POST":
        name=r.POST.get('name')
        data.name=name
        data.save()
        return redirect('list_cate') 
    return render(r,'edit_cate.html')

def delete_cate(r,id):
    CategoryModel.objects.get(id=id).delete()
    return redirect ('list_cate')

def productlist(r):
    cse_date = ProductModel.objects.filter(stock = 'Available')
    eee_date = ProductModel.objects.filter(stock = 'Out_of_stock')
    stock = r.GET.get('stock')

    if stock:
        c_data = ProductModel.objects.filter(stock = stock)
    else:
        c_data=ProductModel.objects.all()
    
    context={
        'data':c_data,
        'cse_date':cse_date,
        'eee_date':eee_date,
        'stock':stock
    }
    return render(r,'productlist.html',context)

def productAdd(r):
    product=CategoryModel.objects.all()
    if r.method=="POST":
        name=r.POST.get('name')
        unit_price=int(r.POST.get('unit_price'))
        qty=int(r.POST.get('qty'))
        stock=r.POST.get('stock')
        category=r.POST.get('category')

        total_amount= unit_price*qty

        p_data=CategoryModel.objects.get(id=category)

        ProductModel.objects.create(
            name=name,
            unit_price=unit_price,
            qty=qty,
            stock=stock,
            category=p_data,
            total_amount=total_amount,
        )
        return redirect('productlist')
    context={
        'data':product
    }
    return render(r,'productAdd.html',context)

def productEdit(r,id):
    product=CategoryModel.objects.all()
    data=ProductModel.objects.get(id=id)
    if r.method=="POST":
        name=r.POST.get('name')
        unit_price=int(r.POST.get('unit_price'))
        qty=int(r.POST.get('qty'))
        stock=r.POST.get('stock')
        category=r.POST.get('category')
        total_amount=unit_price*qty

        p_data=CategoryModel.objects.get(id=category)

        data.name=name
        data.unit_price=unit_price
        data.qty=qty
        data.stock=stock
        data.category=p_data
        data.total_amount=total_amount
        data.save()
        return redirect('productlist')
    context={
        'data':data,
        'product':product
    }

    return render (r,'productEdit.html',context)

def productDelete(r,id):
    ProductModel.objects.get(id=id).delete()
    return redirect('productlist')
