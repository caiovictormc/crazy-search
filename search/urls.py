from django.conf.urls import url
from search.views import ModelList, ModelDetail, ModelDelete, ModelCreate, ModelUpdate, ModelAutocomplete
from . import views

app_name = 'search'
urlpatterns = [
    url(r'^$', ModelList.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', ModelDetail.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', ModelDelete.as_view(), name='delete'),
    url(r'^create/$', ModelCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', ModelUpdate.as_view(), name='update'),
    url(r'^model-autocomplete/$', ModelAutocomplete.as_view(), name='model-autocomplete'),
    url(r'^results/$', views.modelresults, name='results'),
]
