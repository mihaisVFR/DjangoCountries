from django.shortcuts import render, HttpResponse
import json
from myapp.models import Country, Language

# Create your views here.
with open('countries.json') as file:
   lands_and_langs = json.load(file)

def home(request):
    return render(request, "index.html")


def countries(request):
    lands = Country.objects.all()
    context = {'countries': lands}
    return render(request, "countries-list.html", context)


def country(request, name=""):
    land = Country.objects.get(country=name)
    language = land.languages.all()
    context = {"country": land,
               "languages": language
               }
    return render(request, "country_page.html", context)


def languages(request):
    langs = Language.objects.all()
    context = {"langs": langs}
    return render(request, "languages.html", context)


def del_from_db(cls):
    cls.objects.all().delete()

#del_from_db(Language)



