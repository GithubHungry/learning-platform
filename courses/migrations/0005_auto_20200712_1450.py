# Generated by Django 3.0.8 on 2020-07-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200712_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='title',
            field=models.CharField(default='No title', max_length=225),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='No title', max_length=225),
        ),
        migrations.AddField(
            model_name='text',
            name='title',
            field=models.CharField(default='No title', max_length=225),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='No title', max_length=225),
        ),
    ]
