"""studentdatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'main'

urlpatterns = [
    path("", views.homepage, name = 'homepage'),
    path("register/", views.register, name = 'register'),
    path("logout/", views.logout_request, name = 'logout'),
    path("login/", views.login_request, name = 'login'),
    path("addstudent/", views.addstudent, name = 'addstudent'),
    path("updatestudent/<str:pk>/", views.updatestudent, name = 'updatestudent'),
    path("deletestudent/<str:pk>/", views.deletestudent, name = 'deletestudent'),
    path("academics/<str:pk>/", views.StudentInfoDetailView.as_view(), name='academics'),
    path("searchstudent/", views.searchstudent, name = 'searchstudent'),
    path('websearch/', views.websearch, name='websearch'),
    path('websearch/search', views.search, name='search'),
    path("edit_profile/", views.UserEditView.as_view(), name = 'edit_profile'),
    path("password/", views.PasswordsChangeView.as_view(template_name = 'main/change-password.html')),
]
