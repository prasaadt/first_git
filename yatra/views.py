from django.http import HttpResponse
from django.shortcuts import render


def contact(request):
    return render(request,'contact.html')
def home(request):
    return render(request,'index.html')
def Products(request):
    return HttpResponse('''"these are our products" <br> <a href="http://127.0.0.1:8000"> Home <a/>''')
def about(request):
    return render(request,'about.html')
def planatour(request):
    return render(request,'Plan_a_tour.html')
