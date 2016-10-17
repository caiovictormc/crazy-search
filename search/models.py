from django.db import models


class MyModel(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["-number"]

    def __str__(self):
        return self.name
