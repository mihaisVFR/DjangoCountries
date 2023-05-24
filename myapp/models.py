from django.db import models
import json


with open('countries.json') as file:
    lands_and_langs = json.load(file)

class Language(models.Model):
    language = models.CharField(max_length=35)

# Create your models here.
class Country (models.Model):
   country = models.CharField(max_length=35)
   languages = models.ManyToManyField(to=Language)


def add_country():
    for land_and_lang in lands_and_langs:
       count = Country(country=land_and_lang["country"])
       count.save()



def add_language():
    langs_unique = []
    for land_and_lang in lands_and_langs:
        land = Country.objects.get(country=land_and_lang["country"])
        for langs in land_and_lang["languages"]:
            if langs not in langs_unique:
                langs_unique.append(langs)
                lang = Language(language=langs)
                lang.save()
                land.languages.add(lang)


