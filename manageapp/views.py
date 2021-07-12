import django_filters
from rest_framework import viewsets,filters
from rest_framework.views import APIView
from .models import Project,Todo
from .serializer import ProjectSerializer,TodoSerializer
from rest_framework.response import Response

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    filter_fields=('id','deadline','name','isComplete')

class TodoViewSet(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    filter_fields=('id','todoNo')