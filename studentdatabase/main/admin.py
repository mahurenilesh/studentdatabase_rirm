from dataclasses import fields
from django.contrib import admin
from .models import StudentInfo
from django.db import models
# Register your models here.


class StudentInfoAdmin(admin.ModelAdmin):
    fieldsets = [
                ("Student Information", {"fields":["StudentRollNumber","StudentName","StudentClass","StudentSchool","StudentMobile","StudentAddress"]}),
                ("Student Academics", {"fields":["MathMarks","PhysicsMarks","ChemistryMarks","BioMarks","EnglishMarks"]}),

    ]

admin.site.register(StudentInfo, StudentInfoAdmin)
