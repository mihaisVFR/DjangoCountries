from django.db import models
import json

# FIXME: в этом файле должны быть ТОЛЬКО модели, прочие функции размещать тут не стоит
with open('countries.json') as file:
    lands_and_langs = json.load(file)

class Language(models.Model):
    # FIXME: может свойство стоило назвать "name"? Это же название языка.
    language = models.CharField(max_length=35)

# FIXME: форматируйте код согласно PEP-8
# Create your models here.
class Country (models.Model):
   country = models.CharField(max_length=35)
   languages = models.ManyToManyField(to=Language)


def add_country():
    for land_and_lang in lands_and_langs:
       count = Country(country=land_and_lang["country"])
       count.save()

def add_languages():
    langs_unique = []
    for land_and_lang in lands_and_langs:
        for langs in land_and_lang["languages"]:

            if langs not in langs_unique:
                langs_unique.append(langs)
                language = Language(language=langs)
                language.save()

def add_communications():
    for land_and_lang in lands_and_langs:
        land = Country.objects.get(country=land_and_lang["country"])
        for langs in land_and_lang["languages"]:
            lang = Language.objects.get(language=langs)
            land.languages.add(lang)



