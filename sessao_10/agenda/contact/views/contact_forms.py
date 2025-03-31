from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext as _

from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    form_action = reverse("contact:create")
    if request.method == "POST":
        form = ContactForm(request.POST)
        context = {
            "form": form,
            "form_action": form_action,
            "title": _("Create Contact"),
            "html_language": translation.get_language(),
        }

        if form.is_valid():
            # form.save()
            # não salva no banco de dados, mas fica salvo na memória
            contact = form.save(commit=False)
            # contact.show = False
            contact.save()
            return redirect("contact:update", contact_id=contact.pk)
        return render(
            request,
            "contact/create.html",
            context,
        )

    context = {
        "form": ContactForm(),
        "form_action": form_action,
        "title": _("Create Contact"),
        "html_language": translation.get_language(),
    }
    return render(
        request,
        "contact/create.html",
        context,
    )


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse("contact:update", args=(contact_id,))
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        context = {
            "form": form,
            "form_action": form_action,
            "title": _("Update Contact"),
            "html_language": translation.get_language(),
        }

        if form.is_valid():
            # form.save()
            # não salva no banco de dados, mas fica salvo na memória
            contact = form.save(commit=False)
            # contact.show = False
            contact.save()
            return redirect("contact:update", contact_id=contact.pk)
        return render(
            request,
            "contact/create.html",
            context,
        )

    context = {
        "form": ContactForm(instance=contact),
        "form_action": form_action,
        "title": _("Update Contact"),
        "html_language": translation.get_language(),
    }
    return render(
        request,
        "contact/create.html",
        context,
    )
