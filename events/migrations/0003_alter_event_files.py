# Generated by Django 4.2.1 on 2023-05-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0002_alter_event_files"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="files",
            field=models.ImageField(upload_to="events/images/"),
        ),
    ]
