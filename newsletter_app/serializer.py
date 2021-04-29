from rest_framework.serializers import ModelSerializer
from newsletter_app.models import Newsletters
from tags_app.serializer import TagSerializer
from users_app.serializer import UserSerializer


class ViewNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'


class CreateNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'
