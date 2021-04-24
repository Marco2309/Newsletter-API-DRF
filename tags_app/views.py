from rest_framework.viewsets import ModelViewSet
from tags_app.serializer import Tag, TagSerializer
from rest_framework.permissions import AllowAny


class TagsViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
