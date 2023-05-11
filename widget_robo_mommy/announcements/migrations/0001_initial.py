# Generated by Django 4.1.7 on 2023-03-05 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dashboard', '0002_widgetuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('pub_datetime', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.widgetuser')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Like', max_length=5, null=True)),
                ('tally', models.IntegerField(blank=True, default=0, null=True)),
                ('announcement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='announcements.announcement')),
            ],
        ),
    ]
