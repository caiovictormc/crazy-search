from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, DeleteView
from search.models import MyModel

class ModelList(ListView):
    model = MyModel
    context_object_name = "MyModel"
    template_name = "home.html"
    paginate_by = 100

class ModelDetail(DetailView):
    queryset = MyModel.objects.all()
    template_name = "detail.html"

class ModelDelete(DeleteView):
    model = MyModel
    template_name = "delete.html"
