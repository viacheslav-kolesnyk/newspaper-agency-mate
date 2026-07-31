from django import forms
from newspaper.models import Topic
from django.contrib.auth import get_user_model
from newspaper.models import Newspaper


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter topic name"}),
        }

class NewspaperForm(forms.ModelForm):
    editors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Newspaper
        fields = ["title", "content", "published_date", "topic", "editors"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "published_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "topic": forms.Select(attrs={"class": "form-select"}),
        }
