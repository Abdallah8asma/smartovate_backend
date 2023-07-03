from rest_framework import serializers
from .models import Team
from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True) 
    class Meta:
        model = TeamMember
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    teammember = TeamMemberSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = '__all__'
