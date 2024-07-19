# items/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, index

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', index, name='index'),  # Handle the root URL
    path('api/', include(router.urls)),
]
