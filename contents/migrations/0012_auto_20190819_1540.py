# Generated by Django 2.2.2 on 2019-08-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0011_projectimage_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_ended',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='date_started',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
