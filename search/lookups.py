from selectable.base import ModelLookup
from selectable.registry import registry

from .models import MyModel


class MyModelLookup(ModelLookup):
    model = MyModel
    search_fields = ('name')

registry.register(MyModelLookup)
