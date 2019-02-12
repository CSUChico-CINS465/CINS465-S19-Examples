from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

from . import models

def index(request):
    i_list = models.Suggestion.objects.all()
    n_list = []
    for item in i_list:
        n_list += [item.suggestion_field + "2"]
    context = {
        "body":"Hello World Template Variable",
        "title":"Title Hello",
        "item_list":n_list
    }
    return render(request, "page.html", context=context)

def page_view(request, page):
    i_list = []
    p_range = page*10
    for i in range(20*(page+1)):
        i_list += ["Item "+str(i)]
    context = {
        "body":"Hello World Template Variable",
        "title":"Title Hello",
        "item_list":i_list[p_range:p_range+10],
        "page":page,
        "next":page+1
    }
    return render(request, "page.html", context=context)
