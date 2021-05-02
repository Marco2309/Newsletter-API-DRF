from rest_framework.viewsets import ModelViewSet
from tags_app.serializer import Tag, TagSerializer
from rest_framework.permissions import AllowAny
from users_app.permissions import NotPermissions
from django.core.exceptions import ObjectDoesNotExist
from users_app.models import CustomUser

class TagsViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            try:
                user = self.request.user
                admin = CustomUser.objects.get(
                    groups__name__in=['administrador'], id=user.id)
            except ObjectDoesNotExist:
                self.permission_classes = [NotPermissions, ]
        return super(TagsViewSet, self).get_permissions()
