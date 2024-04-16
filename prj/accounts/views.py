from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    from django.shortcuts import render
    from rest_framework import viewsets
    from rest_framework import permissions

    from education.serializers import *
    from education.models import *

    class SchoolViewset(viewsets.ModelViewSet):
        queryset = School.objects.all()
        serializer_class = SchoolSerializer

    class SClassViewset(viewsets.ModelViewSet):
        queryset = SClass.objects.all()
        serializer_class = SClassSerializer

    class StudentViewest(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer