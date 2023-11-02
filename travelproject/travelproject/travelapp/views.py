from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,People

# Create your views here.
# def demo(request):
#      name='india'
#      # return HttpResponse("hello world")
#      return render(request,"home.html",{'obj':name})
# def index(request):
#     return render(request,'home.html',)
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     z=x+y
#     return render(request,'result.html',{'result':z})
# def contact(request):
#     return render(request,'contact.html')


def index(request):
    obj=Place.objects.all()
    obj1 = People.objects.all()

    return render(request,'index.html',{'result':obj,'result1':obj1})