# Generated by Django 4.2.4 on 2024-07-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='is_completed',
            field=models.BooleanField(),
        ),
    ]
