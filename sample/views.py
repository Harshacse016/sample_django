from django.shortcuts import render
from django.http import HttpResponse
from .models import Numbers
# Create your views here.

def home(request):

    obj = Numbers()
    obj.num1 = "Enter first number"
    obj.num2 = "Enter the second number"

    return render(request,'index.html',{'numbers':obj}) 

                                # or 

    #return render(request,'index.html',{'num1':"Enter first number",'num2':"Enter the second number"})
    # the above one num1 and num2 are dynamically allocating the names to index.html
    # return HttpResponse("hello world")

def add(request):

    # num1 = request.GET["num1"]
    # num2 = request.GET["num2"]

    num1 = request.POST["num1"]
    num2 = request.POST["num2"]

    res = int(num1) + int(num2)

    return render(request,'result.html',{'result':res})