from rest_framework import serializers
from .models import Pageindex,FeedbackClient

class PageindexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pageindex
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackClient
        fields = ('id','name','avatar','description',)

