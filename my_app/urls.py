from django.urls import path

from my_app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('index',views.index,name="index"),
    path('kai',views.kai,name="kai"),
    path('food',views.Food_add,name="food")
]