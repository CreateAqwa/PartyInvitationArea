from django.db import models

class data (models.Model):
    name=models.CharField(max_length=20 )
    mobno=models.CharField(max_length=10 ,default='')
    
    city=models.CharField(max_length=50, default='')
    address=models.CharField(max_length=50, default='')
    
    Photo=models.ImageField(upload_to="static/invited", default='')
    partydate=models.CharField(max_length=50, default='')
    
# Create your models here.
