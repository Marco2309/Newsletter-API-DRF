from rest_framework.routers import DefaultRouter
from tags_app.views import TagsViewSet

router = DefaultRouter()
router.register('', TagsViewSet)
urlpatterns = router.urls
