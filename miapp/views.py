from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def PrimVist(request):
        return render(request,'Nuevo Documento de texto.html')

def SegunVist(request):
        return render(request,'moreinfo.html')

def TercerVist(request):
        return render(request,'pag-3.html')