from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(AboutMe)
class AboutMeTranslationOptions(TranslationOptions):
    fields = ('bio','profession','about_me')


@register(MainWorld)
class MainWorldTranslationOptions(TranslationOptions):
    fields = ('profession', 'main_text', 'follower')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('feedback',)


@register(Consultation)
class ConsultationTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'duration', 'format', 'feedback')


@register(Consultation_Keys)
class Consultation_keysTranslationOptions(TranslationOptions):
    fields = ('keys',)







