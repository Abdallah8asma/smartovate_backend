from modeltranslation.translator import TranslationOptions
from .models import About
from modeltranslation.translator import translator


class AboutTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "meta_title", "meta_description", "description", "long_description")


translator.register(About, AboutTranslationOptions)
