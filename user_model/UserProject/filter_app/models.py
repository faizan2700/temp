from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=20) 

    class Meta: 
        db_table = 'Manufacturer' 

    def __str__(self):
        return str(self.name) 
    
    def __repr__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=25) 
    price = models.DecimalField(max_digits=5, decimal_places=2) 
    description = models.TextField()
    release_date = models.DateField() 
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE) 

    class Meta:
        db_table = 'Product' 

    def __str__(self):
        return str(self.name) 

    def __repr__(self):
        return str(self.name) 

