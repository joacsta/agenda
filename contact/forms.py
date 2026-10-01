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
        help_text="digite seu número de telefone aqui".capitalize(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            message = ValidationError(
                "primeiro nome não pode ser igual ao segundo".capitalize(),
                code="invalid",
            )
            self.add_error("first_name", message)
            self.add_error("last_name", message)
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name == "ABC":
            self.add_error(
                "first_name", ValidationError("veio do add_error", code="invalid")
            )
        return first_name


def create(request: HttpRequest):
    if request.method == "POST":
        context = {"form": ContactForm(request.POST)}
        return render(request, "contact/create.html", context)

    context = {"form": ContactForm(request.POST)}
    return render(request, "contact/create.html", context)
