# Generated by Django 5.0.2 on 2025-07-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningplatform', '0003_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
