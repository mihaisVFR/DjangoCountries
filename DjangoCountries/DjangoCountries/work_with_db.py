from myapp.models import Country, Language
import json

with open('countries.json') as file:
    lands_and_langs = json.load(file)


def add_country():
    for land_and_lang in lands_and_langs:
        count = Country(country=land_and_lang["country"])
        count.save()


def add_language():
    langs_unique = []
    for land_and_lang in lands_and_langs:
        for langs in land_and_lang["languages"]:
            if langs not in langs_unique:
                langs_unique.append(langs)
    i = 1
    for lang in langs_unique:
        langs = Language(id=i, language = lang, primary_key = True)
        langs.save()


def del_from_db():
    Country.objects.all().delete()


add_country()
add_language()
