from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from search.models import MyModel

class ModelList(ListView):
    model = MyModel
    context_object_name = "MyModel"
    template_name = "home.html"
