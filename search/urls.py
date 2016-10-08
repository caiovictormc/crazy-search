from django.conf.urls import url
from search.views import ModelList

app_name = 'search'
urlpatterns = [
    url(r'^home/$', ModelList.as_view(), name='home')
]
