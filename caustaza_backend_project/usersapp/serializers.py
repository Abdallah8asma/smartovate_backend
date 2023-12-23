from rest_framework import serializers
from sm_core.user_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email','username','password']
