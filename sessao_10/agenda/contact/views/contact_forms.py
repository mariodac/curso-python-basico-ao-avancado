from django.shortcuts import render
from django import forms
from django.utils import translation
from django.utils.translation import gettext as _

from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email',)

def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST),
            'title': _('Create Contact'),
            'html_language': translation.get_language(),
        }
        return render(
            request,
            'contact/create.html',
            context,
        )
        

    context = {
        'form': ContactForm(),
        'title': _('Create Contact'),
        'html_language': translation.get_language(),
    }
    return render(
        request,
        'contact/create.html',
        context,
    )