from newsletter_app.serializer import Newsletters, NewsletterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from tags_app.serializer import TagSerializer
from rest_framework.response import Response
from rest_framework import status
 


class NewslettersViewSet(ModelViewSet):
    queryset = Newsletters.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (AllowAny,)

    @action(methods=['GET'], detail=True)
    def tags(self, request, pk=None):
        print(request.user)
        newsletter = self.get_object()
        tags = newsletter.tags.all()
        serialized = TagSerializer(tags, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
