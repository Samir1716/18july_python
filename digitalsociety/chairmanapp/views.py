from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'chairmanapp/index.html')

def about(request):
    return render(request,'chairmanapp/about.html')