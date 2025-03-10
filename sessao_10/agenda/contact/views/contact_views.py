from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import translation
from django.utils.translation import gettext as _
from django.db.models import Q
from django.core.paginator import Paginator

from contact.models import Contact

def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': _('Contacts'),
        'html_language': translation.get_language(),
        'page_obj': page_obj,
    }
    return render(
        request,
        'contact/index.html',
        context,
    )


def contact(request, contact_id):
    # consultando sem shortcuts
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # if single_contact is None:
    #     raise Http404

    # consultando com shortcuts
    # single_contact = get_object_or_404(Contact, pk=contact_id)
    single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id, show=True))
    contact_name = f'{single_contact.first_name} {single_contact.last_name}'
    context = {
        'contact': single_contact,
        'title': f"{_('Contact')} {contact_name}",
        'html_language': translation.get_language(),
    }
    return render(
        request,
        'contact/contact.html',
        context,
    )


def search(request):
    search_term = request.GET.get('query', '').strip()
    if search_term == '':
        return redirect('contact:index')
    contacts = Contact.objects.all().filter(show=True).filter(Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term) | Q(phone__icontains=search_term) | Q(email__icontains=search_term)).order_by('id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': _('Search'),
        'html_language': translation.get_language(),
        'search_term': search_term
    }
    return render(
        request,
        'contact/index.html',
        context,
    )