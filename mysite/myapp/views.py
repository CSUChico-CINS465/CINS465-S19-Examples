from django.shortcuts import render, redirect
# from django.utils.html import escape
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



from django.http import JsonResponse
# import json
# Create your views here.

from . import models
from . import forms

@login_required(redirect_field_name='/', login_url="/login/")
def index(request):
    #Form Submission
    if request.method == "POST":
        form_instance = forms.SuggestionForm(request.POST)
        if form_instance.is_valid():
            print(request.POST)
            # message = escape(form_instance.cleaned_data['suggestion_field'])
            new_sugg = models.Suggestion()
            new_sugg.suggestion_field = form_instance.cleaned_data["suggestion_field"]
            new_sugg.save()
            form_instance = forms.SuggestionForm()
    else:
        form_instance = forms.SuggestionForm()
    #initial page load
    if request.method == "GET":
        print("GET")
    i_list = models.Suggestion.objects.all()
    # n_list = []

    # for item in i_list:
    #     n_list += [item.suggestion_field + "2"]
    context = {
        "body":"Hello World Template Variable",
        "title":"Title Hello",
        "item_list":i_list,
        "form":form_instance
    }
    return render(request, "page.html", context=context)

@login_required(login_url="/login/")
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

def suggestions_json(request):
    i_list = models.Suggestion.objects.all()
    resp_list = {}
    resp_list["suggestions"] = []
    for item in i_list:
        resp_list["suggestions"] += [{"suggestion":item.suggestion_field}]
    return JsonResponse(resp_list)

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            user = form_instance.save()
            return redirect("/login/")
            # print("Hi")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)
