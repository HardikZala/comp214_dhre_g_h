from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import *
from datetime import datetime

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def list_staff(request):
    staffs = Staff.objects.all().values()
    template = loader.get_template('list_staff.html')
    context={
        'staffs': staffs
    }
    return HttpResponse(template.render(context, request))

def list_branch(request):
    branches = Branch.objects.all().values()
    template = loader.get_template('list_branch.html')
    context={
        'branches': branches
    }
    return HttpResponse(template.render(context, request))

def list_clients(request):
    clients = Client.objects.all().values()
    template = loader.get_template('list_clients.html')
    context={
        'clients': clients
    }
    return HttpResponse(template.render(context, request))

##def hire_staff(request):
  ##  template = loader.get_template('hire_staff.html')
    ##return HttpResponse(template.render())

def hire_staff(request):
    template = loader.get_template('hire_staff.html')
    if request.method == 'POST':
        staffno = request.POST['staffno']
        fname = request.POST['fname']
        lname = request.POST['lname']
        position = request.POST['position']
        sex = request.POST['sex']
        dob = request.POST['dob']
        salary = request.POST['salary']
        branchno = request.POST['branchno']
        telephone = request.POST['telephone']
        mobile = request.POST['mobile']
        email = request.POST['email']

        staff = Staff()
        staff.hire_staff(staffno, fname, lname, position,sex, dob, salary, branchno, telephone, mobile, email)
        return render(request, 'hire_staff.html')
    return render(request, 'hire_staff.html')
        

def update_staff(request):
    print(request.POST)
    if request.method == 'POST':
        staffno = request.POST['staffno']
        salary = request.POST['salary']
        telephone = request.POST['telephone']
        mobile = request.POST['mobile']
        email = request.POST['email']

        staff = Staff()
        staff.update_staff(staffno, salary, telephone, mobile, email)
    
        return HttpResponse("Staff updated successfully")