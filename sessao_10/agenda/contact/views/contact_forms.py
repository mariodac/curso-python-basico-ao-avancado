from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext as _

from contact.forms import ContactForm

def create(request):
    if request.method == "POST":
        context = {
            "form": ContactForm(request.POST),
            "title": _("Create Contact"),
            "html_language": translation.get_language(),
        }
        return render(
            request,
            "contact/create.html",
            context,
        )

    context = {
        "form": ContactForm(),
        "title": _("Create Contact"),
        "html_language": translation.get_language(),
    }
    return render(
        request,
        "contact/create.html",
        context,
    )
