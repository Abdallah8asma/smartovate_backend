from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from .serializers import UserSerializer

class UsersViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

        return Response({"message": "Failed to add user"}, status=status.HTTP_400_BAD_REQUEST)
