from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):
    deadline = models.IntegerField(default=-1)
    name = models.CharField(max_length=32)
    isComplete = models.BooleanField(default=False)
    memo=models.CharField(max_length=256)
    order = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(2)] )
    orderBy=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(2)])


class Todo(models.Model):
    todoNo = models.ForeignKey(Project,related_name='todo',on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    deadline = models.IntegerField(default=-1)
    priority = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    isComplete = models.BooleanField(default=False)