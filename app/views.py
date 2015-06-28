from django.shortcuts import render, redirect
from django.http import HttpResponse
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
    employee.save()

    return HttpResponse('done')


# list all employees
def list_employee(request):
    employees = Employee.objects.all()

    data = {'employees': employees}

    return render(request, 'employee/list.html', data)


# edit employee
def edit_employee(request, key):        # key is the 'id' column, 'id' keyword already exists

    employee = Employee.objects.get(key)

    if not employee:
        return redirect('homepage')
    else:
        data = {'employee': employee, 'found': 'true'}

        return render(request, 'employee/create.html', data)


# update employee
def update_employee(request):

    key = Session['userId']

    if not key:
        return HttpResponse('invalid')
    else:
        employee = Employee.objects.get(key)

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
def delete_employee(request, key):
    employee = Employee.objects.get(key)

    if not employee:
        return HttpResponse('invalid')
    else:
        employee.delete()

        return HttpResponse('done')
