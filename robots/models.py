from django.db import models
from django.utils import timezone
from  django.forms import SelectDateWidget


class Arm(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name="Модель руки",
    )

    def __str__(self):
        return self.name

#
# class Location(models.Model):
#     country = models.CharField(max_length=)