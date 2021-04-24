from rest_framework.routers import DefaultRouter
from users_app.views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet)
urlpatterns = router.urls
