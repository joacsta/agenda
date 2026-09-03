from django.shortcuts import render
from django.http import HttpRequest
from contact.models import Contact


def index(request: HttpRequest):
    contacts = Contact.objects.all()
    context = {"contacts": contacts}
    return render(request, 'contact/index.html', context)
