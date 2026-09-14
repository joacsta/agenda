from django.urls import path

from . import views

app_name = "contact"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/<int:contact_id>/", views.single_contact, name="single_contact"),
    path("search/", views.search, name="search"),
    ]
