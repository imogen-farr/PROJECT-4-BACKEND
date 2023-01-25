from django.db import models


class Lifespan(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"
