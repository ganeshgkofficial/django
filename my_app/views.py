from django.shortcuts import render, redirect

from my_app.forms import food_forms
from my_app.models import Food


# Create your views here.
def home(request):

    return render(request,"views.html")

def index(request):

     return render(request,"index.html")

def kai(request):

    return render(request,"kai.html")

def Food_add(request):
    form = food_forms()
    if request.method == 'POST':
        data = food_forms(request.POST)
        if data.is_valid():
            data.save()
    return render(request,"food.html",{'form':form})

#view
def food_view(request):
    data = Food.objects.all()
    return render(request, "view_data.html",{'data': data})

#delete
def food_delete(request,id):
    data = Food.objects.get(id=id)
    data.delete()
    return redirect("viewfood")

#update
def food_update(request,id):
    data = Food.objects.get(id=id)
    form = food_forms(instance = data)
    if request.method == 'POST':
        data = food_forms(request.POST,instance=data)
        if data.is_valid():
            data.save()
    return render(request,"update.html",{'form':form})
