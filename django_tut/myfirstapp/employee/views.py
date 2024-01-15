from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def employee_home(request):
    # return HttpResponse('Employee home page')
    emps = Employee.objects.all()
    return render(request,"employee/home.html",{
        'emps':emps
    })

def add_emp(request):
    # return HttpResponse('Employee home page')
    if request.method == 'POST':
        print('data is coming')

        # fetch data
        emp_name = request.POST.get("empname")
        emp_id = request.POST.get("empid")
        emp_phone = request.POST.get("empphone")
        emp_add = request.POST.get("empadd")
        emp_work = request.POST.get("working")
        emp_depart = request.POST.get("empdepart")

        # validate

        # create model object and set the data
        e = Employee(name=emp_name,emp_id = emp_id, phone=emp_phone, address=emp_add, working = emp_work, department = emp_depart)
        if e.working == None:
            e.working = False
        else:
            e.working = True
        
        # save the object
        e.save()


        # prepare a message

        
        return redirect('/employee/home/')
    return render(request,"employee/add_emp.html",{})


def delete_emp(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/employee/home/")

def update_emp(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    return render(request,"employee/update_emp.html",{'emp':emp})

def do_update_emp(request,emp_id):
        # fetch data
    if request.method == 'POST':
        emp_name = request.POST.get("empname")
        emp_id_temp = request.POST.get("empid")
        emp_phone = request.POST.get("empphone")
        emp_add = request.POST.get("empadd")
        emp_work = request.POST.get("working")
        emp_depart = request.POST.get("empdepart")

        e = Employee.objects.get(pk=emp_id)
        e = Employee(name=emp_name,emp_id = emp_id_temp, phone=emp_phone, address=emp_add, working = emp_work, department = emp_depart)
        if e.working == None:
            e.working = False
        else:
            e.working = True
        
        e.save()

    return redirect('/employee/home/')
    