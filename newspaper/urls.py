
from django.urls import path

from newspaper.views import (
    IndexView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    EditorListView,
    EditorDetailView,
    EditorCreateView,
    EditorUpdateView,
    EditorDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    # Topic patterns
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),

    # Newspaper patterns
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),

    # Editor patterns
    path("editors/", EditorListView.as_view(), name="editor-list"),
    path("editors/<int:pk>/", EditorDetailView.as_view(), name="editor-detail"),
    path("editors/create/", EditorCreateView.as_view(), name="editor-create"),
    path("editors/<int:pk>/update/", EditorUpdateView.as_view(), name="editor-update"),
    path("editors/<int:pk>/delete/", EditorDeleteView.as_view(), name="editor-delete"),
]

app_name = "newspaper"
