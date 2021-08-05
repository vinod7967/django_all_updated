# Generated by Django 3.2.6 on 2021-08-05 06:45

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('relations_app', '0004_alter_student1_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
            ],
            managers=[
                ('student', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='user2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=20)),
                ('subj_name', models.CharField(max_length=20)),
                ('user', models.ManyToManyField(to='relations_app.user2')),
            ],
        ),
    ]
