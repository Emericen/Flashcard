# Generated by Django 3.1.6 on 2021-03-05 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_auto_20210303_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tutorial_video', models.FileField(upload_to='tutorial_videos')),
                ('collection', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='flashcards.collection')),
            ],
        ),
        migrations.AddField(
            model_name='flashcard',
            name='knowledge',
            field=models.ManyToManyField(to='flashcards.Knowledge'),
        ),
    ]
