# items/views.py
# items/views.py

from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def index(request):
    return HttpResponse("Welcome to the Items API. Use the /api/items/ endpoint to interact with the API.")

