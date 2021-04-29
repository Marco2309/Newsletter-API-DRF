from newsletter_app.serializer import ViewNewsletterSerializer, CreateNewsletterSerializer, Newsletters, DetailNewsletterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from users_app.permissions import UserPermissions, NotPermissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ModelViewSet
from tags_app.serializer import TagSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import status


class NewslettersViewSet(ModelViewSet):
    queryset = Newsletters.objects.all()
    serializer_class = ViewNewsletterSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailNewsletterSerializer
        if self.request.method == 'POST':
            return CreateNewsletterSerializer
        return ViewNewsletterSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            try:
                user = self.request.user
                admin = User.objects.get(
                    groups__name__in=['administrador'], id=user.id)
            except ObjectDoesNotExist:
                self.permission_classes = [NotPermissions, ]

        if self.request.method == 'PATCH':
            self.permission_classes = [IsAuthenticated, ]

        return super(NewslettersViewSet, self).get_permissions()

    @action(methods=['GET'], detail=True)
    def tags(self, request, pk=None):
        newsletter = self.get_object()
        tags = newsletter.tags.all()
        serialized = TagSerializer(tags, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(methods=['PATCH'], detail=True)
    def vote(self, request, pk=None):
        id = request.user.id
        newsletter = self.get_object()
        newsletter.voters.add(id)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['PATCH'], detail=True)
    def subscribe(self, request, pk=None):
        id = request.user.id
        newsletter = self.get_object()
        if newsletter.target <= len(newsletter.voters.all()):
            newsletter.users.add(id)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
