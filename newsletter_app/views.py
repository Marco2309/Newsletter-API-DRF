from newsletter_app.serializer import Newsletters, NewsletterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class NewslettersViewSet(ModelViewSet):
    queryset = Newsletters.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (AllowAny,)
