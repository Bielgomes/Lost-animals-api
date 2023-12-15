from rest_framework.serializers import ModelSerializer

from accounts.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserMeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'phone']