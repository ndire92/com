# Generated by Django 4.1.6 on 2023-06-13 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_userprofile_first_name_userprofile_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='reset_password_token',
        ),
    ]