# Generated by Django 3.2 on 2023-03-06 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20230304_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='forumpost',
            new_name='forum_post',
        ),
    ]