from django.core.mail import send_mail
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User, Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserVerifySerializer(ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'is_active', 'groups')


class UserSerializer(ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'groups')


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'last_login', 'username', 'first_name',
                  'last_name', 'email', 'date_joined')

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
        user.groups.add(2)
        send_mail(
            'Bienvenido al Sistema',
            'Gracias por registrarte',
            'hola@hotmail.com',
            [validated_data['email']],
            fail_silently=False
        )
        return user


class CreateAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'last_login', 'username', 'first_name',
                  'last_name', 'email', 'date_joined')

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
        user.groups.add(1)
        return user


class UserForNewsletterSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)
