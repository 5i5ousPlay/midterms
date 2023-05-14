# Generated by Django 3.2 on 2023-05-14 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('onsite', 'Onsite'), ('online', 'Online'), ('hybrid', 'Hybrid')], max_length=6)),
                ('venue', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100)),
                ('target_datetime', models.DateTimeField()),
                ('estimated_hours', models.FloatField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='assignments.course')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widget_Calendar.location')),
            ],
        ),
    ]
