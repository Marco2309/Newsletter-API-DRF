from rest_framework.serializers import ModelSerializer
from tags_app.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagForNewsletterSerializer(ModelSerializer):
  
    class Meta:
        model = Tag
        fields = ('nombre',)