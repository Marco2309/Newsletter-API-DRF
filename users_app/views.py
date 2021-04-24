from users_app.serializer import UserSerializer, CreateUserSerializer, User, CreateAdminSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_administrador=False)
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return UserSerializer


class AdminViewSet(ModelViewSet):
    queryset = User.objects.filter(is_administrador=True)
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAdminSerializer
        return UserSerializer
