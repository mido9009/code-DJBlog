# Generated by Django 4.2 on 2023-11-06 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_date2',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
