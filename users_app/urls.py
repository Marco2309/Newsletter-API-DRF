from rest_framework.routers import DefaultRouter
from users_app.views import UserViewSet, AdminViewSet
from django.urls import path

router = DefaultRouter()
router.register('admin', AdminViewSet)
router.register('', UserViewSet)
urlpatterns = router.urls