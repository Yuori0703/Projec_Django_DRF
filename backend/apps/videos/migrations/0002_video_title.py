# Generated by Django 5.1.5 on 2025-02-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='no title', max_length=256),
        ),
    ]
