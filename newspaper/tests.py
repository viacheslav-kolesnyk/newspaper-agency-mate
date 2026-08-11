from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Newspaper
from newspaper.forms import EditorCreationForm


Editor = get_user_model()


class EditorAndFormTests(TestCase):

    def setUp(self):
        self.user = Editor.objects.create_user(
            username="staff_editor",
            password="password123"
        )
        self.client.login(username="staff_editor", password="password123")
        self.topic = Topic.objects.create(name="Sports")

    # 1. REVISED EDITOR REGISTRATION FORM TEST
    def test_editor_registration_form_validation(self):
        # Form validation check for editor creation with invalid data
        form_data = {
            "username": "",  # Обов'язкове поле пусте
            "password": "short",
        }
        form = EditorCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)


class NewspaperCRUDTests(TestCase):
    """Full CRUD coverage for Newspaper"""

    def setUp(self):
        self.user = Editor.objects.create_user(
            username="author_editor",
            password="password123"
        )
        self.client.login(username="author_editor", password="password123")
        self.topic = Topic.objects.create(name="Tech")

        # Initial newspaper for update/deletion tests
        self.newspaper = Newspaper.objects.create(
            title="Original Title",
            content="Original Content",
            editor=self.user,
            published_date="2026-08-02"
        )
        self.newspaper.topics.add(self.topic)

    # 2. NEWSPAPER CREATION TEST (C)
    def test_newspaper_create_view(self):
        create_url = reverse("newspaper:newspaper-create")
        form_data = {
            "title": "Brand New Article",
            "content": "Fresh content for the tech section.",
            "published_date": "2026-08-02",
            "topics": self.topic.id,
            "editor": self.user.id
        }

        response = self.client.post(create_url, data=form_data)
        self.assertEqual(response.status_code, 302)  # Успішний редірект
        self.assertTrue(Newspaper.objects.filter(title="Brand New Article").exists())

    # 3. NEWSPAPER UPDATE TEST (U)
    def test_newspaper_update_view(self):
        update_url = reverse("newspaper:newspaper-update", kwargs={"pk": self.newspaper.pk})
        form_data = {
            "title": "Updated Title",
            "content": "Updated Content text.",
            "published_date": "2026-08-02",
            "topics": self.topic.id,
            "editor": self.user.id
        }

        response = self.client.post(update_url, data=form_data)
        self.assertEqual(response.status_code, 302)

        self.newspaper.refresh_from_db()
        self.assertEqual(self.newspaper.title, "Updated Title")

    # 4. NEWSPAPER DELETION TEST (D)
    def test_newspaper_delete_view(self):
        delete_url = reverse("newspaper:newspaper-delete", kwargs={"pk": self.newspaper.pk})

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Newspaper.objects.filter(pk=self.newspaper.pk).exists())
