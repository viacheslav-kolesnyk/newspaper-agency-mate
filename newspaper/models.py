from django.db import models
from django.contrib.auth.models import AbstractUser


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

class Editor(AbstractUser):
    # Overriding AbstractUser allows you to add custom fields later if needed
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "editor"
        verbose_name = "editors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    # Many-to-one relationship (one editor per newspaper)
    editor = models.ForeignKey(Editor, on_index=True, on_delete=models.CASCADE, related_name="newspapers")
    # Many-to-many relationship (optional task feature)
    topics = models.ManyToManyField(Topic, related_name="newspapers")

    def __str__(self):
        return self.title
