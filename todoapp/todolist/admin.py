from django.contrib import admin
from . import models
from django.contrib.auth.models import User

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "content", "date")

admin.site.register(models.TodoList, TodoListAdmin)