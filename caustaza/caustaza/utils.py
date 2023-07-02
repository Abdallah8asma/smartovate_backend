import string
from translate import Translator
from django.utils.text import slugify
from django.core.mail import EmailMessage
import threading

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
            if field_name == 'image':
                translated_item[field_name] = field_value.url if field_value else None
            elif isinstance(field_value, (int, float)):
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
    
class EmailThread(threading.Thread):
    """
    Custom thread class for sending emails asynchronously.
    """

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class EmailUtil:
    @staticmethod
    def send_email(data):
        """
        Send an email using the provided data.

        Args:
            data (dict): A dictionary containing email data.
                - email_subject (str): The subject of the email.
                - email_body (str): The body of the email.
                - to_email (str): The recipient's email address.
        """
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()