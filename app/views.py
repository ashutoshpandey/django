from django.shortcuts import render, redirect, RequestContext
from django.http import HttpResponse
import time
from django.contrib.sessions.models import Session
from .models import Employee


def homepage(request):
    return render(request, 'home.html', {
        'name': 'Ashutosh',
        'age': 35,
    })

#--------------- employee methods -------------
# put two line gaps between functions


# create employee from
def create_employee(request):
    return render(request, 'employee/create.html')


# save new employee
def save_employee(request):

    employee = Employee()

    name = request.POST.get('name')
    gender = request.POST.get('gender')

    employee.name = name
    employee.gender = gender

    created_time = time.localtime(time.time())
    employee.created_at = str(created_time.tm_year) + '-' + str(created_time.tm_mon) + '-' + str(created_time.tm_mday)

    employee.save()

    return HttpResponse('done')


# list all employees
def list_employee(request):
    employees = Employee.objects.all()

    data = {'employees': employees}

    return render(request, 'employee/list.html', data)


# edit employee
def edit_employee(request, employee_id):        # key is the 'id' column, 'id' keyword already exists

    employee = Employee.objects.get(id=employee_id)

    if not employee:
        return redirect('homepage')
    else:

        request.session['userId'] = employee.id

        data = {'employee': employee, 'found': 'true'}

        return render(request, 'employee/edit.html', data)


# update employee
def update_employee(request):

    employee_id = request.session['userId']

    if not employee_id:
        return HttpResponse('invalid')
    else:
        employee = Employee.objects.get(id=employee_id)

        if not employee:
            return HttpResponse('invalid')
        else:
            name = request.POST.get('name')
            gender = request.POST.get('gender')

            employee.name = name
            employee.gender = gender
            employee.save()

            return HttpResponse('done')


# delete employee
def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if not employee:
        return redirect('/myapp/list')
    else:
        employee.delete()

        return redirect('/myapp/list')
