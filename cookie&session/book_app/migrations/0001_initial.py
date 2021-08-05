# Generated by Django 3.2.4 on 2021-07-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(default=None, max_length=30)),
                ('movie_name', models.CharField(max_length=30)),
                ('ticket_no', models.IntegerField()),
                ('no_of_tickets', models.IntegerField()),
            ],
        ),
    ]
