from django.db import transaction
from rest_framework import serializers

from .models import (
    School, 
    ClassRoom, 
    Teacher, 
    Student, 
    TeacherClassRoom,
)


class WriteOnlySchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        
    # @transaction.atomic
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     name = validated_data.get('name')
    #     acronym = validated_data.get('acronym')
    #     address = validated_data.get('address')
  
    #     data = {
    #         'name': name,
    #         'acronym': acronym,
    #         'address': address,
    #     }
        
    #     school = School.objects.create(
    #         **data
    #     )
        
    #     return school
    

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        

class ClassRoomSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField()
    grade_and_section_display = serializers.SerializerMethodField()
    school = SchoolSerializer()
    class Meta:
        model = ClassRoom
        fields = '__all__'
        
    def get_grade(self, obj):
        return obj.get_grade_display()
    
    def get_grade_and_section_display(self, obj):
        return obj.get_full_grade_and_section_display()
    
class WriteOnlyClassRoomSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    class Meta:
        model = ClassRoom
        fields = '__all__'
        
class SchoolDetailSerializer(serializers.ModelSerializer):
    # classrooms = ClassRoomSerializer(many=True)
    classroom_count = serializers.IntegerField(read_only=True)
    teacher_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)
    
    
    class Meta:
        model = School
        fields = '__all__'

class ClassRoomForTeacherSerializer(serializers.ModelSerializer):
    classroom = ClassRoomSerializer()
    class Meta:
        model = TeacherClassRoom
        # fields = '__all__'
        exclude = ('id', 'teacher',)

class TinyClassRoomForTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClassRoom
        fields = ('classroom', )

class TeacherSerializer(serializers.ModelSerializer):
    classrooms = TinyClassRoomForTeacherSerializer(many=True)
    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'gender', 'classrooms')
    
    
        
class TeacherDetailSerializer(TeacherSerializer):
    classrooms = ClassRoomForTeacherSerializer(many=True, read_only=True)   


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class StudentDetailSerializer(StudentSerializer):
    classroom = ClassRoomSerializer()
    
class TinyTeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'
        
class TeacherForClassRoomSerializer(serializers.ModelSerializer):
    teacher = TinyTeacherSerializer()
    class Meta:
        model = TeacherClassRoom
        # fields = '__all__'
        exclude = ('id', 'classroom',)
        
class ClassRoomDetailSerializer(ClassRoomSerializer):
    teachers = TeacherForClassRoomSerializer(many=True)
    students = StudentSerializer(many=True)
    