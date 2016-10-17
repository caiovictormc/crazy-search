from django.conf.urls import url

from . import views

app_name = 'search'
urlpatterns = [
    url(r'^$',
        views.ModelList.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.ModelDetail.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        views.ModelDelete.as_view(), name='delete'),
    url(r'^create/$',
        views.ModelCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$',
        views.ModelUpdate.as_view(), name='update'),
    url(r'^model-autocomplete/$',
        views.ModelAutocomplete.as_view(), name='model-autocomplete'),
    url(r'^results/$',
        views.modelresults, name='results'),
]
