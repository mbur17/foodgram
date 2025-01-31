from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls', namespace='users')),
    path('api/', include('recipes.urls', namespace='recipes')),
    path('api/', include('shortener.urls', namespace='shortener'))
]
