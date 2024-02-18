from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def home(request):
     info = ComapanyInformation.objects.first()
     flower = Flower.objects.filter(category__name = 'bg')
   
     data ={
      
        'info':info,
        'flower':flower
    }
     return render(request, 'home.html',data)
    
def about(request):
    info = ComapanyInformation.objects.first()
    flower = Flower.objects.all()
   
    data ={
      
        'info':info,
        'flower':flower
    }
   
    
    return render(request, 'about.html',data)

def contact_us(request):
   return render(request,'contact.html')

def valentines(request):
     info = ComapanyInformation.objects.first()
     flower = Flower.objects.filter(category__name = 'Valentines')
   
     data ={
      
        'info':info,
        'flower':flower
    }
     return render(request,'valentines.html', data)
 
def birthday(request):
     info = ComapanyInformation.objects.first()
     flower = Flower.objects.filter(category__name = 'Birthday')
   
     data ={
      
        'info':info,
        'flower':flower
    }
     return render(request,'birthday.html', data)
 
def special(request):
     info = ComapanyInformation.objects.first()
     flower = Flower.objects.filter(category__name = 'Special')
   
     data ={
      
        'info':info,
        'flower':flower
    }
     return render(request,'special.html', data)
 
def graduation(request):
     info = ComapanyInformation.objects.last()
     flower = Flower.objects.filter(category__name = 'graduation')
   
     data ={
      
        'info':info,
        'flower':flower
    }
     return render(request,'graduation.html', data)