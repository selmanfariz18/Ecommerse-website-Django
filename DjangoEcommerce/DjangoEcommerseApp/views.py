from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demopage(request):
    return HttpResponse("demo page")

def demopageTemplate(request):
    return render(request,"demo.html")

def adminLogin(request):
    return render(request,"admin_templates/signin.html")