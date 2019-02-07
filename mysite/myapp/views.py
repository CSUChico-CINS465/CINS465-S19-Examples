from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    i_list=[]
    for i in range(200):
        i_list += ["Item "+str(i)]
    context = {
        "body":"Hello World Template Variable",
        "title":"Title Hello",
        "item_list":i_list[:10]
    }
    return render(request,"base.html", context=context)

def page(request, page):
    i_list=[]
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
    return render(request,"page.html", context=context)
