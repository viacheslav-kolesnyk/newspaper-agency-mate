from django import forms
from newspaper.models import Topic, Newspaper


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter topic name"}),
        }

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ["title", "content", "published_date", "topics", "editor"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "published_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "topics": forms.CheckboxSelectMultiple,
            "editor": forms.Select(attrs={"class": "form-select"}),
        }
