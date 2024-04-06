from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Staff

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