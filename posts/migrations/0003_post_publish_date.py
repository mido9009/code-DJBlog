# Generated by Django 4.2 on 2023-11-06 20:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
