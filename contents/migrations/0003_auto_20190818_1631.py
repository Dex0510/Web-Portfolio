# Generated by Django 2.2.2 on 2019-08-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20190818_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.CharField(default='https://github.com/Dex0510', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(default='https://www.linkedin.com/in/harshit-mathur-115184162/', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_no',
            field=models.CharField(max_length=20),
        ),
    ]
