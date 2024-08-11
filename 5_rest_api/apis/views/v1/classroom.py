from rest_framework import viewsets, status
from rest_framework.response import Response
from apis.models import ClassRoom
from apis.serializers import ClassRoomSerializer, ClassRoomDetailSerializer, WriteOnlyClassRoomSerializer
from apis.filters import ClassRoomFilter
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.parsers import FormParser, MultiPartParser
from .mixins import APIMixin


class ClassRoomViewSet(APIMixin, viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    filterset_class = ClassRoomFilter
    permission_classes = [AllowAny, ]
    ACTION_SERIALIZERS = {
        'list': ClassRoomSerializer,
        'retrieve': ClassRoomDetailSerializer,
        'create': WriteOnlyClassRoomSerializer,
        'update': WriteOnlyClassRoomSerializer,
        'partial_update': WriteOnlyClassRoomSerializer,
        'destroy': ClassRoomSerializer,
    }
    
    def get_queryset(self):
        return super().get_queryset()

    def get_serializer_class(self):
        return self.ACTION_SERIALIZERS.get(self.action)
    

