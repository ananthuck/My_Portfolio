from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# def phello(request):
#     return HttpResponse("Hello World!")

def index(request):
    return render(request, 'index.html')

def loginpage2(request):
    return render(request,'loginpage2.html')
