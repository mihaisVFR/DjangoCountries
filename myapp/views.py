from django.shortcuts import render
from myapp.models import Country, Language


# Create your views here.
def home(request):
    return render(request, "index.html")


def countries(request):
    lands = Country.objects.all()
    context = {'countries': lands,
               }
    return render(request, "countries-list.html", context)


def country(request, name=""):
    land = Country.objects.get(country=name)
    language = land.languages.all()
    context = {"country": land,
               "languages": language
               }
    return render(request, "country_page.html", context)


def language(request, name=""):
    lang = Language.objects.get(name=name)
    countries = lang.country_set.all()
    context = {"countries": countries,
               "language": lang
               }
    return render(request, "language_page.html", context)


def languages(request):
    langs = Language.objects.all()
    context = {"langs": langs}
    return render(request, "languages.html", context)
