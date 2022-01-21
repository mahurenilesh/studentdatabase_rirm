from dataclasses import field
from pyexpat import model
from turtle import textinput
from typing import Text, TextIO
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from.models import *

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class StudentInfoForm(forms.ModelForm):
    StudentRollNumber = forms.CharField(label='Roll Number')
    StudentName  = forms.CharField(label='Name')
    StudentClass  = forms.CharField(label='Class Name')
    StudentSchool  = forms.CharField(label='School Name')
    StudentMobile = forms.IntegerField(label='Mobile Number')
    StudentAddress  = forms.CharField(label='Address')
    MathMarks  = forms.IntegerField(label='Math Marks')
    PhysicsMarks = forms.IntegerField(label='Physics Marks')
    ChemistryMarks  = forms.IntegerField(label='Chemistry Marks')
    BioMarks  = forms.IntegerField(label='Biology Marks')
    EnglishMarks = forms.IntegerField(label='English Marks') 


    class Meta:
        model = StudentInfo
        #fields = '__all__'
        fields = ["StudentRollNumber", "StudentName",  "StudentClass",  "StudentSchool",  "StudentMobile",  "StudentAddress",  "MathMarks",  "PhysicsMarks",  "ChemistryMarks",  "BioMarks",  "EnglishMarks"]

    def clean_StudentRollNumber(self): # Validates the Computer Name Field
        StudentRollNumber = self.cleaned_data.get('StudentRollNumber')
        if (StudentRollNumber == ""):
            raise forms.ValidationError('This field cannot be left blank')

        for instance in StudentInfo.objects.all():
            if instance.StudentRollNumber == StudentRollNumber:
                raise forms.ValidationError(StudentRollNumber + ' is already added')
    
        return StudentRollNumber

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'date_joined')
