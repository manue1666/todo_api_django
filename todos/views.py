from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(deleted=False)
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"])
    def me(self, request):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(deleted=False)
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get("user")
        user = User.objects.get(id=user_id)
        serializer.save(user=user)
        