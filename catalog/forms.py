# newspaper/forms.py
from django import forms
from newspaper.models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter topic name"}),
        }
