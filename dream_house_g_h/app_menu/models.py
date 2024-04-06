from django.db import models

# Create your models here.

class Staff(models.Model):
    staffno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    DOB = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    branchno = models.DecimalField(max_digits=8, decimal_places=2)
    telephone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'DH_STAFF'


class Branch(models.Model):
    branchno = models.AutoField(primary_key=True)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)

    class Meta:
        db_table = 'DH_BRANCH'
