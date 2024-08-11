from .abstract_models import (
    AbstractSchool,
    AbstractClassRoom,
    AbstractStudent,
    AbstractTeacher,
    AbstractTeacherClassRoom,
    Grade
)
from django.db import models


class School(AbstractSchool):
    pass


class ClassRoom(AbstractClassRoom):
    
    
    def get_grade_display(self):
        return Grade.GRADES.get(self.grade)
    
    def get_full_grade_and_section_display(self):
        return f'{self.get_grade_display()}/{self.section}'


class Teacher(AbstractTeacher):
    pass


class TeacherClassRoom(AbstractTeacherClassRoom):
    pass
    

class Student(AbstractStudent):
    pass
    
 




