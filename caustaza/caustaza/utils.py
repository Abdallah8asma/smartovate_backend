import string
from translate import Translator
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random_string_generator.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
    




def translate_data(data):
    target_languages = ['fr', 'en']  # French and English languages
    translated_data = []
    for item in data:
        translated_item = {}
        for field in item._meta.fields:
            field_name = field.name
            field_value = getattr(item, field_name)
            if isinstance(field_value, (int, float)):
                translated_item[field_name] = field_value
            else:
                translated_item[field_name] = {}
                for language in target_languages:
                    try:
                        translator = Translator(to_lang=language)
                        translated_field_value = translator.translate(str(field_value))
                        translated_item[field_name][language] = translated_field_value
                    except UnicodeDecodeError:
                        # Handle the UnicodeDecodeError, for example, by providing a default value
                        translated_item[field_name][language] = 'Translation not available'
        translated_data.append(translated_item)
    return translated_data
    
