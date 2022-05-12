from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50) 
    number = models.IntegerField() 

    class Meta:
        db_table = 'Car'

class Students(models.Model):
    name = models.CharField(max_length=100) 
    address = models.CharField(max_length=100) 

    class Meta:
        db_table = 'Student'