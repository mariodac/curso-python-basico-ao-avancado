import string
from random import SystemRandom
from django.utils.text import slugify
def random_letters(size=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=size
    ))

def slugify_new(text, k=5):
    return slugify(text) + '-' + random_letters(k)
