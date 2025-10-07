from django.utils import translation
from site_setup.models import SiteSetup

def context_processor_example(request):
    return {
        'example': 'Hello, World!',
    }

def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()
    return {
        'site_setup': {
            'setup': setup,
            'html_language': translation.get_language(),
        },
    }
