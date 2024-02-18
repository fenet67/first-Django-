from django.db import models

# Create your models here.
class ComapanyInformation(models.Model):
   name  = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self) -> str:
      return self.name

class Flower(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='flowers/')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    price   = models.FloatField(null=True)
    review = models.FloatField(default=0)
    def __str__(self) -> str:
      return self.name
  
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
      return self.name