# Generated by Django 3.2.6 on 2021-08-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='duedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
