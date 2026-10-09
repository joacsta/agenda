from django.http import HttpRequest
from django.shortcuts import render

import contact
from contact.forms import RegisterForm


def register(request: HttpRequest):
    form = RegisterForm()
    context = {"form": form}

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, "contact/register.html", context)
