# Generated by Django 4.1.4 on 2023-01-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_profile',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='user/'),
        ),
    ]
