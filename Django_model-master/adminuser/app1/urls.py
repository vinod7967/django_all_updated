from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('std',views.student),
    path('index',views.index),
    path('about',views.about),
]