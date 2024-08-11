import uuid

from django.db import models
from django.utils import timezone


class Gender:
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    gender_choices = (
        (MALE, 'ผู้ชาย'),
        (FEMALE, 'ผู้หญิง'),
        (OTHER, 'อื่นๆ'),
    )
    
class Grade:
    GRADES = {
        'K1': 'อนุบาล 1',
        'K2': 'อนุบาล 2',
        'K3': 'อนุบาล 3',
        'G1': 'ประถมศึกษา 1',
        'G2': 'ประถมศึกษา 2',
        'G3': 'ประถมศึกษา 3',
        'G4': 'ประถมศึกษา 4',
        'G5': 'ประถมศึกษา 5',
        'G6': 'ประถมศึกษา 6',
        'G7': 'มัธยมศึกษา 1',
        'G8': 'มัธยมศึกษา 2',
        'G9': 'มัธยมศึกษา 3',
        'G10': 'มัธยมศึกษา 4',
        'G11': 'มัธยมศึกษา 5',
        'G12': 'มัธยมศึกษา 6',
    }

    grade_choices = [(key, f'{value} ({key})') for key, value in GRADES.items()]
    
    
    
class AbstractMember(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=10, 
        choices=Gender.gender_choices)
    
    class Meta:
        abstract = True

class AbstractSchool(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
        )
    acronym = models.CharField(
        max_length=10,
        unique=True
        )
    address = models.CharField(
        max_length=255,
        blank=True, 
        null=False
        )
    
    class Meta:
        abstract = True
        
        
    def __str__(self):
        return f'({self.acronym}) {self.name}'
        

class AbstractClassRoom(models.Model):
    school = models.ForeignKey(
        'School', 
        on_delete=models.CASCADE, 
        related_name='classrooms'
        )
    grade = models.CharField(
        max_length=10,
        choices=Grade.grade_choices,
        )
    section = models.CharField(
        max_length=10
        )
    
    class Meta:
        abstract = True
        unique_together = ['school', 'grade', 'section']
        

class AbstractTeacher(AbstractMember):
    
    class Meta:
        abstract = True
        unique_together = ['first_name', 'last_name']
    
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}' 
    

class AbstractTeacherClassRoom(models.Model):
    teacher = models.ForeignKey(
        'Teacher', 
        on_delete=models.CASCADE, 
        related_name='classrooms'
        )
    classroom = models.ForeignKey(
        'ClassRoom', 
        on_delete=models.CASCADE, 
        related_name='teachers'
        )
    
    class Meta:
        abstract = True
        unique_together = ['teacher', 'classroom']


class AbstractStudent(AbstractMember):
    classroom = models.ForeignKey(
        'ClassRoom', 
        on_delete=models.CASCADE, 
        related_name='students'
        )
    
    class Meta:
        abstract = True
        unique_together = ['first_name', 'last_name']
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
   