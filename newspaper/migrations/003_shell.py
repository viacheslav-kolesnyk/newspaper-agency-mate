from django.contrib.auth import get_user_model
from django.db import migrations


def create_test_user(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(username="user").exists():
        User.objects.create_user("user", "user@test.com", "user12345")
def remove_test_user(apps, schema_editor):
    User = get_user_model()
    User.objects.filter(username="user").delete()
class Migration(migrations.Migration):
    dependencies = [
        ("newspaper", "0002_alter_editor_options"),
    ]
    operations = [
        migrations.RunPython(create_test_user, remove_test_user),
    ]
