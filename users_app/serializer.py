from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserVerifySerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'first_name',
        #           'last_name', 'is_active', 'is_administrador' )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('id', 'username', 'email', 'first_name',
        #           'last_name', 'is_active')


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('password', 'last_login', 'username', 'first_name',
        #           'last_name', 'email', 'date_joined', 'is_active')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CreateAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('password', 'last_login', 'username', 'first_name',
        #           'last_name', 'email', 'date_joined')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
