from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions
from caustaza.utils import translate_data

from .models import Team, TeamMember
from .serializers import TeamSerializer, TeamMemberSerializer


class TeamListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = None

    def get(self, request):
        language = request.query_params.get('language', 'en')  # Default language is English ('en')

        # Retrieve all teams from the database
        teams = self.get_queryset()

        # Translate the teams to the desired language
        translated_teams = translate_data(teams)

        # Serialize the translated teams
        serializer = self.get_serializer(translated_teams, many=True)

        # Return the serialized translated teams as JSON response
        return Response(serializer.data)


class TeamMemberListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    pagination_class = None

    def get(self, request):
        language = request.query_params.get('language', 'en')  # Default language is English ('en')

        # Retrieve all team members from the database
        team_members = self.get_queryset()

        # Translate the team members to the desired language
        translated_team_members = translate_data(team_members)

        
        # Return the serialized translated team members as JSON response
        return Response(translated_team_members)
