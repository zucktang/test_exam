from apis.models import Teacher, ClassRoom, TeacherClassRoom
from apis.serializers import TeacherSerializer, TeacherDetailSerializer
from apis.filters import TeacherFilter

from django.db import transaction

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.exceptions import NotFound, ValidationError

from .mixins import APIMixin


class TeacherViewSet(APIMixin, viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter
    permission_classes = [AllowAny, ]
    ACTION_SERIALIZERS = {
        'list': TeacherSerializer,
        'retrieve': TeacherDetailSerializer,
        'create': TeacherSerializer,
        'update': TeacherSerializer,
        'partial_update': TeacherSerializer,
        'destroy': TeacherSerializer,
    }
    
    def get_classroom(self, classroom_id):
        try:
            return ClassRoom.objects.get(pk=classroom_id)
        except ClassRoom.DoesNotExist:
            raise NotFound({'classroom': 'Classroom not found.'})

        

    @transaction.atomic
    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        teacher = self.get_object()
        classroom_id = request.data.get('classroom')

        if not classroom_id:
            raise ValidationError({'classroom': 'This field is required.'})

        classroom = self.get_classroom(classroom_id)

        teacher_classroom, created = TeacherClassRoom.objects.get_or_create(
            teacher=teacher,
            classroom=classroom,
        )

        if not created:
            raise ValidationError({'error': 'Teacher already in this classroom'})

        serializer = TeacherDetailSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    @action(detail=True, methods=['post'])
    def exit(self, request, pk=None):
        teacher = self.get_object()
        classroom_id = request.data.get('classroom')

        if not classroom_id:
            raise ValidationError({'classroom': 'This field is required.'})

        classroom = self.get_classroom(classroom_id)

        try:
            teacher_classroom = TeacherClassRoom.objects.get(
                teacher=teacher,
                classroom=classroom
            )
            teacher_classroom.delete()
        except TeacherClassRoom.DoesNotExist:
            raise NotFound({'error': 'Teacher not in this classroom'})

        serializer = TeacherDetailSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)
