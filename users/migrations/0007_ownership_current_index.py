# Generated by Django 3.1.6 on 2021-03-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210302_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownership',
            name='current_index',
            field=models.IntegerField(default=0),
        ),
    ]