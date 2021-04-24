from rest_framework.serializers import ModelSerializer
from newsletter_app.models import Newsletters


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'
