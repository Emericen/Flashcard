from django.db import models
from django.contrib.auth.models import User
from flashcards.models import Flashcard

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	last_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	date_joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		pass


class Owns(models.Model):
	Owner = models.ForeignKey(User, on_delete=models.CASCADE)
	Flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)

	def __str__(self):
		pass





# Create your models here.

















