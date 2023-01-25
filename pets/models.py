from django.db import models


class Pet(models.Model):  # inside the brackets is where its inheriting from
    name = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=300)
    environments = models.ManyToManyField(
        'environments.Environment', related_name="pets")
    lifespans = models.ManyToManyField(
        'lifespans.Lifespan', related_name="pets")

    def __str__(self):
        return f"{self.name} - {self.animal}"
