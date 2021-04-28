from rest_framework.serializers import ModelSerializer
from newsletter_app.models import Newsletters
from tags_app.serializer import TagSerializer
from users_app.serializer import UserSerializer


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'
