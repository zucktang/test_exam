from django.db.models import Count, OuterRef, Subquery

from rest_framework import viewsets, status
from rest_framework.response import Response
from apis.models import School, ClassRoom

from apis.serializers import SchoolSerializer, SchoolDetailSerializer
from apis.filters import SchoolFilter
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.parsers import FormParser, MultiPartParser
from .mixins import APIMixin


class SchoolViewSet(APIMixin, viewsets.ModelViewSet):
    queryset = School.objects.annotate(
        classroom_count=Count('classrooms'),
        teacher_count=Count(Subquery(
            ClassRoom.objects.filter(id=OuterRef('classrooms__id')).values('teachers').distinct()
        )),
        student_count=Count(Subquery(
            ClassRoom.objects.filter(id=OuterRef('classrooms__id')).values('students').distinct()
        ))
    )
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter
    permission_classes = [AllowAny, ]
    parser_classes = [MultiPartParser, FormParser]
    ACTION_SERIALIZERS = {
        'list': SchoolSerializer,
        'retrieve': SchoolDetailSerializer,
        'create': SchoolSerializer,
        'update': SchoolSerializer,
        'partial_update': SchoolSerializer,
        'destroy': SchoolSerializer,
    }
    
    def get_queryset(self):
        return super().get_queryset()

    def get_serializer_class(self):
        return self.ACTION_SERIALIZERS.get(self.action)
    
    
    

