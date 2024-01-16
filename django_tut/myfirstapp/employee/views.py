from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee,Testimonial

# Create your views here.
def employee_home(request):
    # return HttpResponse('Employee home page')
    emps = Employee.objects.all()
    return render(request,"employee/home.html",{
        'emps':emps
    })

#add new employee data
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

# delete the employee data
def delete_emp(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/employee/home/")

# open up update employee page
def update_emp(request,emp_id):
    emp = Employee.objects.get(pk=emp_id)
    return render(request,"employee/update_emp.html",{'emp':emp})

# update the employee
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
        e.name=emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_add
        e.working = emp_work
        e.department = emp_depart

        if e.working == None:
            e.working = False
        else:
            e.working = True
        
        e.save()

    return redirect('/employee/home/')


# testimonials
def testimonials(request):
    testi = Testimonial.objects.all()
    return render(request,"employee/testimonials.html",{'testi':testi})
    