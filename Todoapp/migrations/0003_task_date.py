# Generated by Django 4.0.4 on 2022-05-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0002_rename_tasks_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-03-30'),
            preserve_default=False,
        ),
    ]
