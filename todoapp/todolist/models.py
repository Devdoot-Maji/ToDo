from django.db import models
from django.utils import timezone

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True) 
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    class Meta:
        ordering = ["-date"]
    def __str__(self):
        return self.title