from rest_framework.serializers import ModelSerializer
from users_app.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'is_administrador')


class CreateAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'last_login', 'username', 'first_name',
                  'last_name', 'email', 'is_active', 'is_administrador', 'date_joined')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_administrador=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
