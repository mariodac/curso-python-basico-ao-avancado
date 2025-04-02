from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext as _

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()
    context = {
        'form': form,
        "title": _("Register User"),
        "html_language": translation.get_language(),
    }
    return render(request, 'contact/register.html', context)