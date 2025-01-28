from django.db import models
from django.utils import timezone


# id (primary key - automático)
# first_name (string), last_name (string), phone (string), 
# email (string), created_date (date), description (string)
# category (foreign key), show(boolean), owner (foreign key)
# picture (image)
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.TextField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
