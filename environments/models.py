from django.db import models


class Environment(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"
