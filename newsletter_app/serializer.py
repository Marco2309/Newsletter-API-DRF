from rest_framework.serializers import ModelSerializer
from newsletter_app.models import Newsletters
from tags_app.serializer import TagForNewsletterSerializer
from users_app.serializer import UserForNewsletterSerializer


class ViewNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'


class DetailNewsletterSerializer(ModelSerializer):
    tags = TagForNewsletterSerializer(many=True)
    users = UserForNewsletterSerializer(many=True)
    members = UserForNewsletterSerializer(many=True)
    voters = UserForNewsletterSerializer(many=True)

    class Meta:
        model = Newsletters
        fields = '__all__'


class CreateNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = ('nombre', 'description', 'frecuencia',
                  'fecha_creacion', 'tags', 'target')


class InviteNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = ('id', 'nombre', 'members')
