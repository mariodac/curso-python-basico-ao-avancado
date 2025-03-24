from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from contact.models import Contact


class ContactForm(forms.ModelForm):
    # Nessa forma pode alterar tudo dentro do campo, pode adicionar até campos que não estão na model
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your last name")}),
        label = _("Your last name"),
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your first name")}),
        label = _("Your first name"),
    )

    # example_field = forms.CharField(
    #     widget=forms.TextInput(attrs={"placeholder": _("Example")}),
    #     help_text= _("Help text")
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["first_name"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
        )
        # widgets = {
        #     "first_name": forms.TextInput(attrs={"placeholder": _("Your first name")}),
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        # self.add_error("first_name", ValidationError(_("Error"), code="invalid"))
        # self.add_error(None, ValidationError(_("Error 2"), code="invalid"))
        # self.add_error(None, ValidationError(_("Error 3"), code="invalid"))
        return super().clean()
