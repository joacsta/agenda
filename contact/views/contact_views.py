from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from contact.models import Contact


def index(request: HttpRequest):
    contacts = Contact.objects.filter(show=True).order_by("-id")[:31]
    context = {"contacts": contacts, "title": "Agenda"}
    return render(request, 'contact/index.html', context)


def single_contact(request: HttpRequest, contact_id: int):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    context = {"contact": contact}
    return render(request, "contact/single_contact.html", context)
