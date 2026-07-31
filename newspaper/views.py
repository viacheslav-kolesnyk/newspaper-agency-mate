from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from newspaper.models import Newspaper, Topic, Editor
from newspaper.forms import NewspaperForm, EditorCreationForm, EditorUpdateForm


class IndexView(generic.TemplateView):
    template_name = "newspaper/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_newspapers"] = Newspaper.objects.count()
        context["num_topics"] = Topic.objects.count()
        context["num_editors"] = Editor.objects.count()
        return context


# ==================== TOPIC VIEWS ====================

class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "newspaper/topic_list.html"
    context_object_name = "topic_list"
    paginate_by = 10


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "newspaper/topic_confirm_delete.html"
    success_url = reverse_lazy("newspaper:topic-list")


# ==================== NEWSPAPER VIEWS ====================

class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "newspaper/newspaper_list.html"
    context_object_name = "newspaper_list"
    paginate_by = 5
    queryset = Newspaper.objects.select_related("topic")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "newspaper/newspaper_detail.html"


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "newspaper/newspaper_confirm_delete.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


# ==================== EDITOR VIEWS ====================

class EditorListView(LoginRequiredMixin, generic.ListView):
    model = Editor
    template_name = "newspaper/editor_list.html"
    context_object_name = "editor_list"
    paginate_by = 10


class EditorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Editor
    template_name = "newspaper/editor_detail.html"
    queryset = Editor.objects.prefetch_related("newspapers__topic")
