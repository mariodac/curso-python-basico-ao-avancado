import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings
from django.core.files import File

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker("pt_BR")
    categories = ["Trabalho", "Cliente", "Serviços", "Amigos", "Família", "Conhecidos"]

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for index in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile["mail"]
        first_name, last_name = profile["name"].split(" ", 1)  # type: ignore
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()  # type: ignore
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)
        if os.name == "nt":
            image_path = os.path.join(os.environ.get("temp"), f"random-image-{index}.jpg")  # type: ignore
        else:
            image_path = os.path.join("/tmp", f"random-image-{index}.jpg")
        with open(image_path, "wb") as image_file:
            file_content = fake.image()
            image_file.write(file_content)
            file_name = os.path.basename(image_path)
        file_name = os.path.basename(image_path)
        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
                picture=File(open(image_path, "rb"), name=file_name),
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
