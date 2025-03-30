from django.shortcuts import redirect, render
from django.utils import translation
from django.utils.translation import gettext as _

from contact.forms import ContactForm

def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        context = {
            "form": form,
            "title": _("Create Contact"),
            "html_language": translation.get_language(),
        }

        if form.is_valid():
            # form.save()
            # não salva no banco de dados, mas fica salvo na memória
            contact = form.save(commit=False)
            contact.show = False
            contact.save()
            return redirect("contact:create")
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
