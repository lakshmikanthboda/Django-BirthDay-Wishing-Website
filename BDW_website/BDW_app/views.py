from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
def BDWfun(request):
    d=request.GET['n']
    img=request.GET['img']
    return render(request, 'bdw.html',{'name':d,'img':img})