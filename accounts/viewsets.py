from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from accounts.models import User
from accounts.serializers import UserSerializer, UserMeSerializer


class UserViweSet(ViewSet):

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserChangePasswordViewSet(ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        pass


class UserMeViewSet(ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request):
        user = User.objects.get(id=request.user.id)

        serializer = UserMeSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        pass

