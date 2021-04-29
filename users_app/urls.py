from rest_framework.routers import DefaultRouter
from users_app.views import UserViewSet, AdminViewSet, verifyLogin
from django.urls import path

router = DefaultRouter()
router.register('admin', AdminViewSet)
router.register('', UserViewSet)
urlpatterns = [path('verify/', verifyLogin), ]
urlpatterns += router.urls
