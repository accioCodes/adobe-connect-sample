# Generated by Django 3.0.8 on 2020-07-27 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qNumber', models.IntegerField()),
                ('sooratesoal', models.TextField(max_length=50)),
                ('numberOftheTestAnswers', models.CharField(max_length=50)),
                ('valueOftheTestAnswers', models.TextField(max_length=100)),
                ('trueAnswer', models.TextField(max_length=50)),
                ('typeTest', models.TextField(max_length=50)),
                ('typeEx', models.TextField(max_length=50)),
                ('extraField', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
                ('url', models.URLField()),
                ('idOftheQuiz', models.IntegerField()),
                ('questions', models.TextField(max_length=300)),
                ('topic', models.CharField(max_length=50)),
                ('extraField', models.TextField(max_length=50)),
                ('startDate', models.DateField()),
                ('startTime', models.TimeField()),
                ('quizDesigner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=300)),
                ('url', models.URLField()),
                ('category', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('startTime', models.TimeField()),
                ('duration', models.DurationField()),
                ('passwordOftheMeeting', models.TextField(max_length=50)),
                ('extraField', models.TextField(max_length=50)),
                ('members', models.TextField(max_length=300)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JoiningtoMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extraField', models.TextField(max_length=50)),
                ('meetingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backprojectapi.Meeting')),
                ('meetingMember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnsweringQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerOfPerson', models.TextField(max_length=300)),
                ('extraField', models.TextField(max_length=50)),
                ('questionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backprojectapi.Question')),
                ('solver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]