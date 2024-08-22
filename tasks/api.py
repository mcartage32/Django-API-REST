from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets, permissions


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer
