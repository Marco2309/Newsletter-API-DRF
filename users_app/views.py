from users_app.serializer import UserSerializer, CreateUserSerializer, User, CreateAdminSerializer, UserVerifySerializer, Group
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from users_app.permissions import UserPermissions, NotPermissions


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(groups__name__in=['usuario'])
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return UserSerializer

    def get_permissions(self):
        try:
            user = self.request.user
            admin = User.objects.get(
                groups__name__in=['administrador'], id=user.id)
        except ObjectDoesNotExist:
            self.permission_classes = [NotPermissions, ]
            return super(UserViewSet, self).get_permissions()

        if self.request.method in ['POST']:
            self.permission_classes = [AllowAny, ]
            return super(UserViewSet, self).get_permissions()

        if self.action == 'list' and not admin:
            self.permission_classes = [UserPermissions, ]
            return super(UserViewSet, self).get_permissions()
        return super(UserViewSet, self).get_permissions()


class AdminViewSet(ModelViewSet):
    queryset = User.objects.filter(groups__name__in=['administrador'])
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAdminSerializer
        return UserSerializer

    def get_permissions(self):
        try:
            user = self.request.user
            admin = user in self.queryset
            print('admin', admin)
        except ObjectDoesNotExist:
            self.permission_classes = [NotPermissions, ]
            return super(AdminViewSet, self).get_permissions()

        if self.request.method == 'POST':
            self.permission_classes = [AllowAny, ]
            return super(AdminViewSet, self).get_permissions()

        if self.request.method == 'GET' and not admin:
            self.permission_classes = [NotPermissions, ]
            return super(AdminViewSet, self).get_permissions()
        return super(AdminViewSet, self).get_permissions()


@api_view(['GET'])
def verifyLogin(request):
    try:
        username = request.user
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = UserVerifySerializer(user)
        return Response(
            status=200,
            data=serialized.data
        )
