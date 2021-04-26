from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from users_app.views import verifyLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verify/', verifyLogin),
    path('user/', include('users_app.urls')),
    path('tags/', include('tags_app.urls')),
    path('newsletter/', include('newsletter_app.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
