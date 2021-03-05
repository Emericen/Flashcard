from django.db import models
from django.utils import timezone
# from django.urls import reverse


class Collection(models.Model):
	label = models.CharField(max_length=20)
	image = models.ImageField(default='default.jpg', upload_to='collection_thumbnails')
	description = models.TextField(default='')

	def __str__(self):
		return self.label


class Knowledge(models.Model):
	collection = models.ForeignKey(Collection, default=None, on_delete=models.CASCADE)
	label = models.CharField(max_length=200)
	description = models.TextField(default='')
	tutorial_video = models.FileField(upload_to='tutorial_videos')

	def __str__(self):
		return f'{self.id}: {self.label[:10]}'



class Flashcard(models.Model):
	front = models.TextField()	# ?
	back = models.TextField()	# ?
	flashcard_type = models.CharField(max_length=2)

	collection = models.ForeignKey(Collection, default=None, on_delete=models.CASCADE)
	knowledge = models.ManyToManyField(Knowledge)

	def __str__(self):
		return f'{self.flashcard_type}: {self.front[:50]}'

	# def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk': self.pk})









