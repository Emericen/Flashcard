from django.db import models

# Create your models here.
class Flashcard(models.Model):
	front = models.TextField()	# ?
	back = models.TextField()	# ?
	flashcard_type = models.CharField(max_length=2)

	def __str__(self):
		pass

