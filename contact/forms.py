from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import render

from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "João",
            }
        ),
        label="Nome",
        help_text="digite seu nome aqui".capitalize(),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Costa",
            }
        ),
        label="Sobrenome",
        help_text="digite seu sobrenome aqui".capitalize(),
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "(61) 99999-0000",
            }
        ),
        label="Telefone",
        help_text="digite seu telefone aqui".capitalize(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone")

    def clean(self):
        self.add_error(
            "first_name", ValidationError("mensagem de erro", code="invalid")
        )
        self.add_error(
            "last_name", ValidationError("outra mensagem de erro", code="invalid")
        )

        return super().clean()


def create(request: HttpRequest):
    if request.method == "POST":
        context = {"form": ContactForm(request.POST)}
        return render(request, "contact/create.html", context)

    context = {"form": ContactForm(request.POST)}
    return render(request, "contact/create.html", context)
