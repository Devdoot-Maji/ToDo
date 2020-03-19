from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    completed = models.BooleanField(default=False) 
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ["-date"]
    def __str__(self):
        return self.title