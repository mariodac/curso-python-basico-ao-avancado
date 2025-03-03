from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext as _
from contact.models import Contact

def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('id')[:10]
    print(contacts.query)
    context = {
        'contacts': contacts,
        'title': _('Contacts'),
        'html_language': translation.get_language(),
    }
    return render(
        request,
        'contact/index.html',
        context,
    )