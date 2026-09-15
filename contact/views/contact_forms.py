# from django.core.paginator import Paginator
# from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render

# from contact.models import Contact


def create(request: HttpRequest):
    if request.method == "POST":
        print(request.POST.get("first_name"))
        print(request.POST.get("last_name"))

    print(request.method)
    context = {}
    return render(request, "contact/create.html", context)
