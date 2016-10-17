from dal import autocomplete

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from search.models import MyModel
from search.forms import MyModelForm


class ModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = MyModel.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class ModelList(ListView):
    model = MyModel
    context_object_name = "MyModel"
    template_name = "search/home.html"
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super(ModelList, self).get_context_data(**kwargs)
        context['forma'] = MyModelForm
        return context

class ModelDetail(DetailView):
    queryset = MyModel.objects.all()
    template_name = "search/detail.html"

class ModelDelete(DeleteView):
    model = MyModel
    template_name = "search/delete.html"
    success_url = "/"

class ModelCreate(CreateView):
    model = MyModel
    fields = ['name', 'number']
    template_name = "search/create.html"
    success_url = "/"

class ModelUpdate(UpdateView):
    model = MyModel
    fields = ['name', 'number']
    template_name = "search/update.html"
    success_url = "/"


def modelresults(request):
    if request.method == "GET":
        form = MyModelForm(request.GET)
        if form.is_valid():
            #reason = dict(form.fields['reason'].choices)[reason]
            pk = form['name'].value()
            mymodel = get_object_or_404(MyModel, pk=pk)
            return render(request, 'search/results.html', {
                'mymodel': mymodel
            })
