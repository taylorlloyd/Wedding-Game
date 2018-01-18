# Generated by Django 2.0.1 on 2018-01-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgserver', '0002_auto_20180106_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='bride_conversions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='flipped',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='groom_conversions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='interactions',
            field=models.IntegerField(default=0),
        ),
    ]
