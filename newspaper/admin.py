from django.contrib import admin
from .models import Topic, Editor, Newspaper


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]

@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "last_name", "years_of_experience"]
    list_filter = ["groups"]
    search_fields = ["username", "first_name", "last_name"]

@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "published_date", "editor"]
    list_filter = ["published_date", "topics"]
    search_fields = ["title", "content"]
    date_hierarchy = "published_date"
