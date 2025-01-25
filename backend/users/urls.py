from django.urls import path, include
from rest_framework import routers

from .views import FoodgramUserViewSet


app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', FoodgramUserViewSet)


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls))
]
