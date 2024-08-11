from django_filters import rest_framework as filters
from .models import School, ClassRoom, Teacher, Student
from .abstract_models import Gender

class SchoolFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

class ClassRoomFilter(filters.FilterSet):
    school = filters.NumberFilter(field_name="school__id")

    class Meta:
        model = ClassRoom
        fields = ['school']

class TeacherFilter(filters.FilterSet):
    classroom = filters.NumberFilter(field_name='classrooms__classroom__id') 
    school = filters.NumberFilter(field_name='classrooms__classroom__school__id') 
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    gender = filters.ChoiceFilter(choices=Gender.gender_choices)

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']

class StudentFilter(filters.FilterSet):
    school = filters.NumberFilter(field_name="classroom__school__id")
    classroom = filters.NumberFilter(field_name='classroom__id') 
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    gender = gender = filters.ChoiceFilter(choices=Gender.gender_choices)

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']