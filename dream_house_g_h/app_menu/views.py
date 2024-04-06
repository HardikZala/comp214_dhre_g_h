from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

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

def hire_staff(request):
    template = loader.get_template('hire_staff.html')
    return HttpResponse(template.render())
