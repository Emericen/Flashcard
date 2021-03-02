# Generated by Django 3.1.6 on 2021-03-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='collection_thumbnail')),
            ],
        ),
        migrations.AddField(
            model_name='flashcard',
            name='collection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='flashcards.collection'),
        ),
    ]
