# Generated by Django 4.1.7 on 2023-03-04 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('course', models.CharField(blank=True, max_length=255, null=True)),
                ('perfect_score', models.IntegerField(blank=True, null=True)),
                ('passing_score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('section', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]