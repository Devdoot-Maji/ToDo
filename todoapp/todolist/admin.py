from django.contrib import admin
from . import models

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "content", "date")

admin.site.register(models.TodoList, TodoListAdmin)
