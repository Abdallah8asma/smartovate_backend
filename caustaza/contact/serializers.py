from rest_framework import serializers
from contact.models import Contact
from caustaza.utils import EmailUtil

# Define the ContactSerializer class
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'phone', 'adress', 'message')

    def create(self, validated_data):
        # Send an email to the user
        email_body = 'Bonjour ' + validated_data['full_name'] + "\n\n Merci d'avoir visité notre Site caustaza  \n nous avons vous repondre le Plutot possible  \n\n Bien Cordialement \n caustaza \n"
        data = {'email_body': email_body, 'to_email': validated_data['email'], 'email_subject': 'Contact'}
        EmailUtil.send_email(data)

        # Send an email to the admin
        email_body = 'Bonjour mr ABDELKALEK  \n Mr/mdme : ' + validated_data['full_name'] + "\n\n Va vous contacter depuis le site caustaza.tn  \n Voici leur messages :  " + validated_data['message'] + " \n Leur informations  :" + validated_data['phone'] + " " + validated_data['email'] + " \n\n Bien Cordialement \n caustaza \n"
        data = {'email_body': email_body, 'to_email': 'abdelkhalek.bakkari@caustaza.com ', 'email_subject': 'Contact'}
        EmailUtil.send_email(data)

        # Create a new Contact object using the validated data
        return Contact.objects.create(**validated_data)
