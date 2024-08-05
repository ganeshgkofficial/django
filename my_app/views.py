from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,"views.html")

def index(request):

     return render(request,"index.html")

def kai(request):

    return render(request,"kai.html")