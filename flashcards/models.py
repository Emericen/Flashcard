from django.db import models
from django.utils import timezone
# from django.urls import reverse


class Flashcard(models.Model):
	front = models.TextField()	# ?
	back = models.TextField()	# ?
	flashcard_type = models.CharField(max_length=2)

	def __str__(self):
		return f'{self.flashcard_type}: {self.front[:50]}'

	# def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk': self.pk})
