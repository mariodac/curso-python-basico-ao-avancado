from django.shortcuts import redirect, render
from django.utils import translation
from django.utils.translation import gettext as _
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

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
            return redirect("contact:login")
        # else:
        #     messages.error(request, _("Error registering user!"))
    return render(
        request,
        "contact/register.html",
        context,
    )

def login_view(request):
    form = AuthenticationForm(request)
    context = {
        "form": form,
        "title": _("Register User"),
        "html_language": translation.get_language(),
    }

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        context.update({"form": form})
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, _("User logged in successfully!"))
            return redirect("contact:index")
        else:
            messages.error(request, _("Invalid Login!"))
    return render(
        request,
        "contact/login.html",
        context,
    )


def logout_view(request):
    auth.logout(request)
    return redirect("contact:login")