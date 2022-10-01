# Generated by Django 4.1.1 on 2022-10-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_exam_institution_alter_exam_school_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssingExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(max_length=255)),
                ('user', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='school_class',
            new_name='course_class',
        ),
    ]
