from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from search.models import MyModel
from search.forms import MyModelForm

class ModelList(ListView):

    model = MyModel
    context_object_name = "MyModel"
    template_name = "home.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super(ModelList, self).get_context_data(**kwargs)
        context['forma'] = MyModelForm
        return context

class ModelDetail(DetailView):
    queryset = MyModel.objects.all()
    template_name = "detail.html"

class ModelDelete(DeleteView):
    model = MyModel
    template_name = "delete.html"
    success_url = "/"

class ModelCreate(CreateView):
    model = MyModel
    fields = ['name', 'number']
    template_name = "create.html"
    success_url = "/"

class ModelUpdate(UpdateView):
    model = MyModel
    fields = ['name', 'number']
    template_name = "update.html"
    success_url = "/"
