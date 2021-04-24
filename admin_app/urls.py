from rest_framework.routers import DefaultRouter
from admin_app.views import AdminViewSet

router = DefaultRouter()
router.register('', AdminViewSet)
urlpatterns = router.urls
