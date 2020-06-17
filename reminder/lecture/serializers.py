from rest_framework import fields
from rest_framework.serializers import ModelSerializer

from .models import Lecture, Professor, Task


class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    deadline = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'])

    class Meta:
        model = Task
        fields = ('name', 'deadline', 'lecture',)
