from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=35)


class Country (models.Model):
    country = models.CharField(max_length=35)
    languages = models.ManyToManyField(to=Language)
