from newsletter_app.serializer import ViewNewsletterSerializer, CreateNewsletterSerializer, Newsletters, DetailNewsletterSerializer, InviteNewsletterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from users_app.permissions import UserPermissions, NotPermissions
from newsletter_app.permissions import EditNewsletterPermissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ModelViewSet
from tags_app.serializer import TagSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from users_app.models import CustomUser
from rest_framework import status
from django.core.mail import send_mail
from newsletter_app.tasks import send_email_suscriptor
from datetime import timedelta
from datetime import datetime, timezone
from tags_app.models import Tag


class NewslettersViewSet(ModelViewSet):
    queryset = Newsletters.objects.all()
    serializer_class = ViewNewsletterSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        var = serializer.save()
        var.user = request.user
        var.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailNewsletterSerializer
        if self.request.method in ['POST', 'PUT']:
            return CreateNewsletterSerializer
        return ViewNewsletterSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            try:
                user = self.request.user
                admin = CustomUser.objects.get(
                    groups__name__in=['administrador'], id=user.id)
            except ObjectDoesNotExist:
                self.permission_classes = [NotPermissions, ]

        if self.request.method == 'PATCH':
            self.permission_classes = [IsAuthenticated, ]
        if self.request.method in ['PUT', 'DELETE']:
            self.permission_classes = [EditNewsletterPermissions, ]
        return super(NewslettersViewSet, self).get_permissions()

    def get_queryset(self):
        filtro = self.request.query_params.get('tag')
        if filtro:
            newsletterValid = self.queryset.filter(
                tags__nombre__contains=filtro)
            return newsletterValid
        return self.queryset

    @action(methods=['GET'], detail=True)
    def tags(self, request, pk=None):
        newsletter = self.get_object()
        tags = newsletter.tags.all()
        serialized = TagSerializer(tags, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(methods=['GET'], detail=False)
    def own(self, request):
        id = request.user.id
        newsletters = self.queryset.filter(user=id)
        serialized = ViewNewsletterSerializer(newsletters, many=True)
        print(newsletters)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(methods=['GET'], detail=False)
    def subscriptions(self, request):
        try:
            subscriptions = request.user.subscriptions.all()
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serialized = ViewNewsletterSerializer(subscriptions, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(methods=['PATCH'], detail=True)
    def vote(self, request, pk=None):
        user = request.user
        id = user.id
        newsletter = self.get_object()
        votes = newsletter.voters.all()
        if user in votes:
            newsletter.voters.remove(id)
            return Response(status=status.HTTP_200_OK, data={"vote": "remove"})
        newsletter.voters.add(id)
        return Response(status=status.HTTP_200_OK, data={"vote": "add"})

    @action(methods=['PATCH'], detail=True)
    def subscribe(self, request, pk=None):
        user = request.user
        id = user.id
        newsletter = self.get_object()
        users = newsletter.users.all()
        if newsletter.target <= len(newsletter.voters.all()):
            if user in users:
                newsletter.users.remove(id)
                return Response(status=status.HTTP_200_OK, data={"subscribe": "remove"})
            newsletter.users.add(id)
            return Response(status=status.HTTP_200_OK, data={"subscribe": "add"})
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'message': 'No ha alcanzado el target requerido'})

    @action(methods=['PATCH'], detail=True)
    def invite(self, request, pk=None):
        user = request.user
        newsletter = self.get_object()
        admin = newsletter.user
        serialized = InviteNewsletterSerializer(newsletter)
        if admin == user:
            id_guests = request.data['guests']
            correos = []
            for id_invited in id_guests:
                try:
                    invited = CustomUser.objects.get(
                        groups__name__in=['administrador'], id=id_invited)
                    newsletter.members.add(invited)
                    correos.append(invited.email)
                    serialized = InviteNewsletterSerializer(newsletter)
                except ObjectDoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND,
                                    data={
                                        'user not found': id_invited,
                                        'Newsletter': serialized.data
                                    })
            send_mail(
                f'{user} te invito a editar',
                f'{user} te invito a editar {newsletter.nombre}',
                'newsletters@hotmail.com',
                correos,
                fail_silently=False
            )
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def tiempoEnvioMensual(self, email, tiempo):

        fecha_envio = datetime.now() + timedelta(days=tiempo)
        send_email_suscriptor.apply_async(
            args=[email],
            eta=fecha_envio
        )

    @action(methods=['POST'], detail=True)
    def emails(self, request, pk=None):
        newsletter = self.get_object()
        tiempo = newsletter.frecuencia

        if(tiempo == 'semanal'):
            tiempo = 7
        elif (tiempo == 'mensual'):
            tiempo = 30
        elif (tiempo == 'anual'):
            tiempo = 365
        else:
            tiempo = 365

        for user in newsletter.users.all():
            print(user.email)
            self.tiempoEnvioMensual(user.email, tiempo)
        return Response(status=200)
