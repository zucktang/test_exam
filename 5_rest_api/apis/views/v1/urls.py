from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import school, student, teacher, classroom

router = DefaultRouter()
router.register(r'school', school.SchoolViewSet, basename='school')
router.register(r'student', student.StudentViewSet, basename='student')
router.register(r'teacher', teacher.TeacherViewSet, basename='teacher')
router.register(r'classroom', classroom.ClassRoomViewSet, basename='classroom')

urlpatterns = [
    path('', include(router.urls)),
]