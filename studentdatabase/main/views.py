from multiprocessing import context
from re import template
from tkinter.tix import InputOnly
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from django.views import generic
from django.views.generic import DetailView
import requests
from bs4 import BeautifulSoup as bs
from django.urls import reverse_lazy


# Create your views here.

def homepage(request):
    return render(request=request,
                    template_name="main/home.html",
                    context={"studentinfo":StudentInfo.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                    "main/register.html",
                    context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, f"Invalid username or password")

        else:
            messages.error(request, f"Invalid username or password")
    form = AuthenticationForm()
    return render(request,
                    "main/login.html",
                    context={"form":form})

def addstudent(request):
    studentinfos = StudentInfo.objects.all()
    form = StudentInfoForm()
    if request.method=="POST":
        form = StudentInfoForm(request.POST or None)
        if form.is_valid():
            form.save()
            #messages.success(request, f"{studentinfos} Added Successfully")
        return redirect('main:homepage')
    return render(request,
                    "main/addstudent.html",
                    context={"studentinfos":studentinfos, "form":form})

def updatestudent(request, pk):
    studentinfos = StudentInfo.objects.get(id=pk)
    form = StudentInfoForm(instance=studentinfos)

    if request.method == "POST":
        form = StudentInfoForm(request.POST, instance=studentinfos)
        if form.is_valid():
            form.save()
            messages.success(request, f"{studentinfos} Updated Successfully")
            return redirect('main:homepage')
        
    return render(request,
                    "main/updatestudent.html",
                    context={"form":form}
                    )

def deletestudent(request, pk):
    studentinfos = StudentInfo.objects.get(id=pk)
    #form = StudentInfoForm(instance=studentinfos)
    if request.method == "POST":
        studentinfos.delete()
        messages.success(request, f"{studentinfos} Deleted Successfully")
        return redirect('main:homepage')
    return render(request,
                    'main/deletestudent.html',
                    {"studentinfos":studentinfos})

class StudentInfoDetailView(DetailView):
    template_name = 'main/academics.html'
    queryset = StudentInfo.objects.all()

def searchstudent(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        studentnames = StudentInfo.objects.filter(StudentName__contains=searched)

        return render(request,
                    'main/searchstudent.html',
                    {"searched":searched, "studentnames":studentnames})
    else:
        return render(request,
                    'main/searchstudent.html',
                    {})

def websearch(request):
    return render(request,
                    'main/websearch.html',
                    {})


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = search
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')

        final_result = []
        for link in soup.find_all('a'):
            result_url = link.get('href')

            final_result.append(result_url)


        context = {
            'final_result': final_result
        }

        return render(request, 'main/search.html', context)

    else:
        return render(request, 'main/search.html')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'main/edit_profile.html'
    success_url = reverse_lazy('main:homepage')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('main:homepage')