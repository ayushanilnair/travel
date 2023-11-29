from django.http import HttpResponse
from django.shortcuts import render
from  . models import Service

# Create your views here.
def demo(request):
    obj=Service.objects.all()
    return render(request,"home.html",{'result':obj})

# def about(request):
#     x =int(request.GET['n1'])
#     y=int(request.GET['n2'])
#     sum=x+y
#     return render(request,'about.html',{'res':sum})

