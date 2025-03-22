from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext as _

def create(request):
    if request.method == 'POST':
        print(request.POST.get('first_name'))
        

    context = {
        'title': _('Create Contact'),
        'html_language': translation.get_language(),
    }
    return render(
        request,
        'contact/create.html',
        context,
    )