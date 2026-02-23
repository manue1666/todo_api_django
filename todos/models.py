from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title
    
