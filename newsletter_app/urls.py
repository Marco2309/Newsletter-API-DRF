from rest_framework.routers import DefaultRouter
from newsletter_app.views import NewslettersViewSet

router = DefaultRouter()
router.register('', Newsletters)
urlpatterns = router.urls
