from django.conf.urls import url
from search.views import ModelList, ModelDetail

app_name = 'search'
urlpatterns = [
    url(r'^$', ModelList.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', ModelDetail.as_view(), name='detail'),
]
