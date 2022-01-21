from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class StudentInfo(models.Model):
    StudentRollNumber = models.CharField(max_length=10)
    StudentName  = models.CharField(max_length=50)
    StudentClass  = models.CharField(max_length=50,null=True)
    StudentSchool  = models.CharField(max_length=50,null=True)
    StudentMobile = models.IntegerField(validators=[MinValueValidator(999999999), MaxValueValidator(9999999999)], null=True)
    StudentAddress  = models.CharField(max_length=50,null=True)
    MathMarks  = models.IntegerField(null=True)
    PhysicsMarks = models.IntegerField(null=True)
    ChemistryMarks  = models.IntegerField(null=True)
    BioMarks  = models.IntegerField(null=True)
    EnglishMarks  = models.IntegerField(null=True)

    def __str__(self):
        return self.StudentRollNumber