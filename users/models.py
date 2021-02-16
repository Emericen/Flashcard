from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from flashcards.models import Flashcard





class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	last_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	owned_flashcards = models.ManyToManyField(Flashcard, through='Ownership')
	date_joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.last_name + self.first_name} Profile'




class Ownership(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '(' + Owner + ',' + Flashcard + ')'






# Create your models here.

















