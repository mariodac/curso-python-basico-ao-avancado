from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
        )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error("first_name", ValidationError(_("Error"), code="invalid"))
        self.add_error(None, ValidationError(_("Error 2"), code="invalid"))
        self.add_error(None, ValidationError(_("Error 3"), code="invalid"))
        return super().clean()
