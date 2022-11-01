# Generated by Django 4.1.1 on 2022-10-23 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_assignexam_source_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignAswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='exam.assignexam')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assing_answers', to='exam.exercise')),
            ],
        ),
    ]
