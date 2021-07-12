from rest_framework import serializers
from .models import Project, Todo


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'deadline', 'name', 'isComplete','memo','order','orderBy')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','todoNo', 'content', 'deadline', 'priority','isComplete')