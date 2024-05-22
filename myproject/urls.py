"""myproject URL Configuration

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
# myproject/urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('submit-forms/', views.submitForm, name = 'submitForm'),
    path('validate/', views.certificate_validation, name='certificate_validation'),
    path('candidate-data/', views.candidate_Data, name = 'candidateData'),
    path('candidate-list/', views.candidate_list, name = 'candidatelist'),
    path('invalid/', views.invalid, name = 'invalidForm')
]

