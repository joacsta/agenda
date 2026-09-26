from django import forms
from django.core.exceptions import ValidationError

# from django.core.paginator import Paginator
# from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render  # , get_object_or_404, redirect

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone")

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            "first_name", ValidationError("Preencha o campo acima.", code="invalid")
        )
        return super().clean()


def create(request: HttpRequest):
    if request.method == "POST":
        context = {"form": ContactForm(request.POST)}
        return render(request, "contact/create.html", context)

    context = {"form": ContactForm()}
    return render(request, "contact/create.html")
