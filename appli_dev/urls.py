from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home', upload_csv, name="upload_csv"),
    path("model", modeles_available, name="model_list" )
]
