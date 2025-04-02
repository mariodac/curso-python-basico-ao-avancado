from django.shortcuts import redirect, render
from django.utils import translation
from django.utils.translation import gettext as _
from django.contrib import messages

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    context = {
        "form": form,
        "title": _("Register User"),
        "html_language": translation.get_language(),
    }

    if request.method == "POST":
        form = RegisterForm(request.POST)
        context.update({"form": form})
        if form.is_valid():
            form.save()
            messages.success(request, _("User registered successfully!"))
            return redirect("contact:index")
        # else:
        #     messages.error(request, _("Error registering user!"))
    return render(
        request,
        "contact/register.html",
        {
            "form": form,
            "title": _("Register User"),
            "html_language": translation.get_language(),
        },
    )
