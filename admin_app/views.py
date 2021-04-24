from admin_app.serializers import UserSerializer, CreateAdminSerializer, User
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class AdminViewSet(ModelViewSet):
    queryset = User.objects.filter(is_administrador=True)
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAdminSerializer
        return UserSerializer
