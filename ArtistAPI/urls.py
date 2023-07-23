from django.urls import path, include
from rest_framework.routers import DefaultRouter
from artists.views import CustomUserCreate
from django.contrib import admin
from rest_framework.authtoken.views import ObtainAuthToken
from artists.views import WorkViewSet, ArtistViewSet
router = DefaultRouter()
router.register(r'works', WorkViewSet, basename='work')
router.register(r'artists', ArtistViewSet, basename='artist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', CustomUserCreate.as_view(), name='user_register'),
    path('api/', include(router.urls)),
    path('api/token/', ObtainAuthToken.as_view(), name='token_obtain'),
]
