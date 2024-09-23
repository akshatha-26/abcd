from django.urls import path
from . import views

urlpattern=[
    path('hello/',views.hello_world,name="hello world")
]