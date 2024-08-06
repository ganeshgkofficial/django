from django.shortcuts import render

from my_app.forms import food_forms


# Create your views here.
def home(request):

    return render(request,"views.html")

def index(request):

     return render(request,"index.html")

def kai(request):

    return render(request,"kai.html")

def Food_add(request):
    form = food_forms()
    print(form)
    return render(request,"food.html",{'form':form})