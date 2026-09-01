import os
import sys
from datetime import date
from pathlib import Path
from random import choice

import django
from django.conf import settings


DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMERO_DE_OBJETOS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings"
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    from faker import Faker

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = Faker("pt_BR")

    categories = ["Amigos", "Família", "Trabalho"]
    django_categories = [Category(name=name) for name in categories]
    django_contacts = []

    for category in django_categories:
        category.save()

    for _ in range(NUMERO_DE_OBJETOS):
        profile = fake.profile()

        email = profile["mail"]
        first_name, last_name = profile["name"].split(" ", 1)
        phone = fake.phone_number()
        created_date: date = fake.date_this_year()
        desc = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=desc,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
