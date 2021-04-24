from rest_framework.routers import DefaultRouter
from newsletter_app.views import NewslettersViewSet

router = DefaultRouter()
router.register('', NewslettersViewSet)
urlpatterns = router.urls
