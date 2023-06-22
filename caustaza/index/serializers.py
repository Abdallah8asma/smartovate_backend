from rest_framework import serializers
from .models import Pageindex,FeedbackClient, newsletter

class PageindexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pageindex
        fields = '__all__'

class FeaadbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackClient
        fields = ('id','name','avatar','description',)

class NewsletterSerializer(serializers.ModelSerializer):   
    class Meta:
        model = newsletter
        fields = ('email',)
    def create(self, validated_data):
        return newsletter.objects.create(**validated_data)