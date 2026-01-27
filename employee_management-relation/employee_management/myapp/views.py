import decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import User, Department, Employee, Salary

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('employee_list')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')
        
        if password == confirm_password:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password)
            user.user_type = user_type
            user.save()
            if user_type == 'employee':
                Employee.objects.create(user=user, designation='New Employee')
            return redirect('login')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    emp_count = Employee.objects.count()
    dept_count = Department.objects.count()
    total_expense = 0
    try:
        salaries = Salary.objects.all()
        for s in salaries:
            try:
                total = s.basic_salary + (s.basic_salary * s.bonus_percentage / 100)
                total_expense += total
            except (decimal.InvalidOperation, TypeError, ValueError):
                pass  # Skip invalid salary calculations
    except Exception:
        total_expense = 0  # Fallback if querying salaries fails

    context = {
        'emp_count': emp_count,
        'dept_count': dept_count,
        'total_expense': total_expense,
        'user_type': request.user.user_type
    }
    return render(request, 'dashboard.html', context)

@login_required
def department_list(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        Department.objects.create(
            name=name,
            description=description
        )
        return redirect('department_list')
    return render(request, 'department_list.html', {'departments': departments})

@login_required
def department_update(request, pk):
    dept = Department.objects.get(pk=pk)
    if request.method == 'POST':
        name_input = request.POST.get('name')
        description_input = request.POST.get('description')
        
        dept.name = name_input
        dept.description = description_input
        dept.save()
        return redirect('department_list')
    return render(request, 'department_form.html', {'department': dept})

@login_required
def department_delete(request, pk):
    department_obj = Department.objects.get(pk=pk)
    department_obj.delete()
    return redirect('department_list')

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        dept_id = request.POST.get('department')
        designation = request.POST.get('designation')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password,
        )
        user.user_type = 'employee'
        user.save()
        
        department_obj = Department.objects.get(id=dept_id)
        
        Employee.objects.create(
            user=user, 
            department=department_obj, 
            designation=designation, 
            phone=phone, 
            address=address
        )
        return redirect('employee_list')
    return render(request, 'employee_list.html', {'employees': employees, 'departments': departments})

@login_required
def employee_update(request, pk):
    emp = Employee.objects.get(pk=pk)
    departments = Department.objects.all()
    if request.method == 'POST':
        dept_id = request.POST.get('department')
        department_obj = Department.objects.get(id=dept_id)
        
        designation = request.POST.get('designation')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        emp.department = department_obj
        emp.designation = designation
        emp.phone = phone
        emp.address = address
        emp.save()
        
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'employee': emp, 'departments': departments, 'edit_mode': True})

@login_required
def employee_delete(request, pk):
    employee_obj = Employee.objects.get(pk=pk)
    user_obj = employee_obj.user
    user_obj.delete()
    return redirect('employee_list')

@login_required
def salary_list(request):
    employees = Employee.objects.all()

    salaries = []
    try:
        if request.user.user_type == 'admin':
            salaries = Salary.objects.all()
        else:
            salaries = Salary.objects.filter(employee__user=request.user)
    except Exception:
        salaries = []  # Fallback if any error in querying

    for s in salaries:
        try:
            basic = s.basic_salary
            bonus_pct = s.bonus_percentage
            bonus_amount = (basic * bonus_pct) / 100
            s.total = basic + bonus_amount
        except (decimal.InvalidOperation, TypeError, ValueError, AttributeError):
            try:
                s.total = s.basic_salary  # Fallback to basic salary if calculation fails
            except (decimal.InvalidOperation, AttributeError):
                s.total = 0  # If even basic_salary fails, set to 0

    if request.method == 'POST':
        try:
            emp_id = request.POST.get('employee')
            employee_obj = Employee.objects.get(id=emp_id)

            basic = float(request.POST.get('basic_salary'))
            bonus = float(request.POST.get('bonus_percentage'))

            Salary.objects.create(
                employee=employee_obj,
                basic_salary=basic,
                bonus_percentage=bonus
            )
            return redirect('salary_list')
        except (ValueError, Employee.DoesNotExist):
            # Handle invalid input or non-existent employee
            pass  # Or add error message

    return render(request, 'salary_list.html', {'salaries': salaries, 'employees': employees})

@login_required
def salary_update(request, pk):
    salary_obj = Salary.objects.get(pk=pk)
    employees = Employee.objects.all()
    
    if request.method == 'POST':
        employee_id_input = request.POST.get('employee')
        basic_salary_input = request.POST.get('basic_salary')
        bonus_percentage_input = request.POST.get('bonus_percentage')
        
        salary_obj.employee_id = employee_id_input
        salary_obj.basic_salary = basic_salary_input
        salary_obj.bonus_percentage = bonus_percentage_input
        
        salary_obj.save()
        return redirect('salary_list')
    return render(request, 'salary_form.html', {'salary': salary_obj, 'employees': employees})

@login_required
def salary_delete(request, pk):
    salary_obj = Salary.objects.get(pk=pk)
    salary_obj.delete()
    return redirect('salary_list')




