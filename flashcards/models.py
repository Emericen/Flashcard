from django.db import models
from django.utils import timezone
# from django.urls import reverse



# Create your models here.
class Flashcard(models.Model):
	front = models.TextField()	# ?
	back = models.TextField()	# ?
	flashcard_type = models.CharField(max_length=2)

	def __str__(self):
		pass

	# def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk': self.pk})
