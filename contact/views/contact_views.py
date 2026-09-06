from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


def index(request: HttpRequest):
    contacts = Contact.objects.filter(show=True).order_by("-id")[:31]
    context = {"contacts": contacts, "site_title": "Contatos -"}
    return render(request, "contact/index.html", context)


def single_contact(request: HttpRequest, contact_id: int):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    site_title = f"{contact.first_name} {contact.last_name} -"
    context = {"contact": contact, "site_title": site_title}
    return render(request, "contact/single_contact.html", context)


def search(request: HttpRequest):
    search_value: str = request.GET.get("q", "").strip()
    if not search_value:
        return redirect("contact:index")

    contacts = (
        Contact.objects.filter(show=True)
        .filter(
            Q(first_name__icontains=search_value)
            | Q(last_name__icontains=search_value)
            | Q(phone__icontains=search_value)
            | Q(email__icontains=search_value)
        )
        .order_by("-id")
    )
    context = {"contacts": contacts, "site_title": "Procurando - "}
    return render(request, "contact/index.html", context)
