from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext as _

def create(request):
    context = {
        'title': _('Contacts'),
        'html_language': translation.get_language(),
    }
    return render(
        request,
        'contact/create.html',
        context,
    )