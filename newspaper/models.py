from django.db import models
from django.contrib.auth.models import AbstractUser


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Editor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="editor_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="editor_set",
        blank=True,
    )

    class Meta:
        verbose_name = "editor"
        verbose_name_plural = "editors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    # Many-to-one relationship
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, related_name="newspapers")
    # Many-to-many relationship (optional task feature)
    topics = models.ManyToManyField(Topic, related_name="newspapers")

    def __str__(self):
        return self.title
