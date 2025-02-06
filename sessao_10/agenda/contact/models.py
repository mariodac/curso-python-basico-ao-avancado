from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# id (primary key - automático)
# first_name (string), last_name (string), phone (string), 
# email (string), created_date (date), description (string)
# category (foreign key), show(boolean), owner (foreign key)
# picture (image)

class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    name = models.CharField(max_length=50, verbose_name=_("Name"))

    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model):
    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
    first_name = models.CharField(max_length=50, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=50, blank=True, verbose_name=_("Last Name"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name=_("Created Date"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    show = models.BooleanField(default=True, verbose_name=_("Show"))
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d', verbose_name=_("Picture"))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Category"))

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

