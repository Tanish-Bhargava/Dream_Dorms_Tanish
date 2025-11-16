from django.db import models

class searchdb(models.Model):
    area_name = models.CharField(max_length=30)
    property_name= models.CharField(max_length=50)
    Location = models.CharField(max_length=500)
    code = models.CharField(max_length=20)
    Aminites = models.CharField(max_length=500)
    distance = models.CharField(max_length=500)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    price = models.CharField(max_length=8)
    prop_description = models.CharField(max_length=1000)
    
    image = models.ImageField(null = True , blank = True,upload_to='images/')
    
    def __str__(self):
        return self.area_name
    
    
class loginn(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
class grapes(models.Model):
    pname = models.CharField(max_length=30)
    pemail = models.CharField(max_length=50)
    property_code = models.CharField(max_length=20)
    comments = models.CharField(max_length=19999)