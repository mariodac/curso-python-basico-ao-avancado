import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


from contact.models import Contact


class ContactForm(forms.ModelForm):
    # primeira forma de adicionar widget ao form
    # Nessa forma pode alterar tudo dentro do campo, pode adicionar até campos que não estão na model
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your last name")}),
        label=_("Last name"),
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Your first name")}),
        label=_("First name"),
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "(DD) 9 9999-9999",
            }
        ),
        label=_("Phone"),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "youremail@serveremail.com"}),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": _("Describe the contact to be saved")}
        ),
        label=_("Description"),
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*",
            }
        ),
        label=_("Picture"),
        required=False,
    )

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
            "description",
            "category",
            "picture",
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
            msg = ValidationError(
                _("First name and last name cannot be the same"), code="invalid"
            )
            self.add_error("first_name", msg)
            self.add_error("last_name", msg)
        if last_name is not None and re.search(r"\d", last_name):
            self.add_error(
                "last_name",
                ValidationError(_("Last name cannot contain numbers"), code="invalid"),
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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        label=_("First name"),
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        label=_("Last name"),
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error(
                "email",
                ValidationError(
                    _("A user with this email already exists."), code="invalid"
                ),
            )

        return email


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text=_("Required."),
        error_messages={
            "min_length": _("First name must have at least 2 characters."),
        },
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text=_("Required."),
        error_messages={
            "min_length": _("Last name must have at least 2 characters."),
        },
    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password 2"),
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=_("Use the same password as before."),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        
        password = cleaned_data.get("password1")
        if password:
            user.set_password(password)

        if commit:
            user.save()
        return user
        
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    "password2",
                    ValidationError(
                        _("The two password fields didn’t match."),
                        code="password_mismatch",
                    ),
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        current_email = self.instance.email

        if email != current_email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    "email",
                    ValidationError(
                        _("A user with this email already exists."), code="invalid"
                    ),
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error("password1", errors)
        return password1
