from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Staff
from django.db import connection


# Create your views here.

def index(request):
    context = {
        'menus': [
            {'name': 'Staff', 'url': 'staff_menu'},
            {'name': 'Branch', 'url': 'branch_menu'},
            {'name': 'Client', 'url': 'client_menu'}
        ]
    }
    return render(request, 'index.html', context)


from django.shortcuts import render

def list_staff(request):
    staffs = Staff.objects.all().values()
    context = {
        'staffs': staffs
    }
    return render(request, 'list_staff.html', context)


def update_staff(request):
    if request.method == 'POST':
        staffno = request.POST.get('staffno')
        salary = request.POST.get('salary')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        with connection.cursor() as cursor:
            cursor.callproc('update_staff_sp', [staffno, salary, telephone, email])

        return redirect('list_staff')

def staff_menu(request):
    template = loader.get_template('staff_menu.html')
    return HttpResponse(template.render())

def branch_menu(request):
    template = loader.get_template('branch_menu.html')
    return HttpResponse(template.render())

def client_menu(request):
    template = loader.get_template('client_menu.html')
    return HttpResponse(template.render())

from django.db import connection

def test_db_connection():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM DH_STAFF FETCH FIRST 1 ROWS ONLY")
        row = cursor.fetchone()
    return row
