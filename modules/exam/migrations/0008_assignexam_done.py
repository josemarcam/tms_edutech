# Generated by Django 4.1.1 on 2022-10-23 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_assignaswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignexam',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
