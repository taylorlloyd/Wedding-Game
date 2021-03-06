# Generated by Django 2.0.1 on 2018-01-18 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgserver', '0003_auto_20180107_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='adult',
        ),
        migrations.RemoveField(
            model_name='player',
            name='gender',
        ),
        migrations.AddField(
            model_name='player',
            name='bride_medical_friend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='bride_school_friend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='came_alone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='family_friend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='from_alberta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='groom_school_friend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='groom_tech_friend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='just_met',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='parent',
            field=models.BooleanField(default=False),
        ),
    ]
