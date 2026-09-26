from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import render

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone")

    def clean(self):
        # cleaned_data = self.cleaned_data

        # for field in self.fields:
        #     self.add_error(field, ValidationError("erro neste campo", code="invalid"))

        return super().clean()


def create(request: HttpRequest):
    if request.method == "POST":
        context = {"form": ContactForm(request.POST)}
        return render(request, "contact/create.html", context)

    context = {"form": ContactForm(request.POST)}
    return render(request, "contact/create.html", context)
