from rest_framework import viewsets
from apis.models import Student
from apis.serializers import StudentSerializer, StudentDetailSerializer
from apis.filters import StudentFilter
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from .mixins import APIMixin


class StudentViewSet(APIMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter
    permission_classes = [AllowAny, ]
    ACTION_SERIALIZERS = {
        'list': StudentSerializer,
        'retrieve': StudentDetailSerializer,
        'create': StudentSerializer,
        'update': StudentSerializer,
        'partial_update': StudentSerializer,
        'destroy': StudentSerializer,
    }
    
    def get_queryset(self):
        return super().get_queryset()
    
    
