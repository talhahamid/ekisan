from django.contrib import admin
from django.urls import path
from . import views

 
urlpatterns = [
    path('',views.deliveryman,name="deliveryman"),

    path('profile/',views.profile,name="profile"),

    path('myproduct/',views.myproduct,name="myproduct"),

    path('productsdelivered/',views.productsdelivered,name="productsdelivered"),

    path('location/<str:farmer_address>/<str:bitter_address>/',views.location,name="location"),
   
]