# Generated by Django 4.2 on 2023-11-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]
