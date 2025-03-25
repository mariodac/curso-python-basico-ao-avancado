import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from contact.models import Contact


class ContactForm(forms.ModelForm):
    # primeira forma de adicionar widget ao form
    # Nessa forma pode alterar tudo dentro do campo, pode adicionar até campos que não estão na model
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your last name")}),
        label=_("Your last name"),
        required=False,
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your first name")}),
        label=_("Your first name"),
    )

    phone = forms.CharField(required=False)

    # example_field = forms.CharField(
    #     widget=forms.TextInput(attrs={"placeholder": _("Example")}),
    #     help_text= _("Help text")
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # segunda forma de adicionar widget ao form
        # self.fields["first_name"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
        )
        # terceira forma de adicionar widget ao form
        # widgets = {
        #     "first_name": forms.TextInput(attrs={"placeholder": _("Your first name")}),
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        if first_name == last_name:
            msg = (
                ValidationError(
                    _("First name and last name cannot be the same"), code="invalid"
                )
            )
            self.add_error("first_name", msg)
            self.add_error("last_name", msg)
        if last_name is not None and re.search(r"\d", last_name):
            self.add_error(
                    "last_name",
                    ValidationError(
                        _("Last name cannot contain numbers"), code="invalid"
                    ),
                )
        # self.add_error("first_name", ValidationError(_("Error"), code="invalid"))
        # self.add_error(None, ValidationError(_("Error 2"), code="invalid"))
        # self.add_error(None, ValidationError(_("Error 3"), code="invalid"))
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name:
            if re.search(r"\d", first_name):
                self.add_error(
                    "first_name",
                    ValidationError(
                        _("First name cannot contain numbers"), code="invalid"
                    ),
                )
        return first_name
