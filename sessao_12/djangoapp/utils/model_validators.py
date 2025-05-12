from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError(('Apenas imagens PNG são permitidas.'))
    
