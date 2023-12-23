# Generated by Django 4.1 on 2023-02-06 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0006_alter_message_options_rename_members_chatroom_member_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="receiver",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipient",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
