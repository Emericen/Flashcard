# Generated by Django 3.1.6 on 2021-02-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.TextField()),
                ('back', models.TextField()),
                ('flashcard_type', models.CharField(max_length=2)),
            ],
        ),
    ]
