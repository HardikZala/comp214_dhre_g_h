from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('list_staff', views.list_staff, name='list_staff'),
    path('staff_menu', views.staff_menu, name ='staff_menu'),
    path('branch_menu', views.branch_menu, name ='branch_menu'),
    path('client_menu', views.client_menu, name ='client_menu'),
    path('update_staff', views.update_staff, name='update_staff'),
]
