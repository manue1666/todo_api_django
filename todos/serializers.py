from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "created_at", "updated_at", "deleted"]
        extra_kwargs = {
            "name": {"required": True},
            "email": {"required": True},
            "password": {"write_only": True, "required": True},
        }


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)
    class Meta:
        model = Task
        fields = ["id", "user", "title", "description", "completed", "created_at", "updated_at", "deleted", "user_id", "user_name"]
        extra_kwargs = {
            "user": {"required": True},
            "title": {"required": True},
        }


