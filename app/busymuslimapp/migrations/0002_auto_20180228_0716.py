# Generated by Django 2.0 on 2018-02-28 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busymuslimapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='uw_waiver',
        ),
    ]