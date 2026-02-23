from django.contrib import admin
from .models import Task
from .models import User

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "completed", "created_at")
    list_filter = ("completed", "created_at")
    search_fields = ("title", "description")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")