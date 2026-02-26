from django.db import models

class Task(models.Model):
    title: str = models.CharField(max_length=100)
    description: str = models.TextField(null=True, blank=True)
    completed: bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title