# Generated by Django 4.1.4 on 2023-06-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0002_alter_user_managers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="name",
            new_name="Firstname",
        ),
        migrations.AddField(
            model_name="user",
            name="Lastname",
            field=models.CharField(default="", max_length=200),
        ),
    ]
