from django.forms import inlineformset_factory
from insta.models import Album, Photo

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
                                           fields=['image', 'title', 'slug'],
                                           extra=2)
