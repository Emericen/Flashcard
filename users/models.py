from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from flashcards.models import Flashcard




# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)

# 	# name = models.CharField(max_length=200)
# 	invitation_code = models.CharField(max_length=4)

# 	last_name = models.CharField(max_length=100)
# 	first_name = models.CharField(max_length=100)

# 	owned_flashcards = models.ManyToManyField(Flashcard, through='Ownership')
# 	date_joined = models.DateTimeField(default=timezone.now)

# 	def __str__(self):
# 		return f'{self.last_name + self.first_name} Profile'


class User(AbstractBaseUser, PermissionsMixin):

	# user_type = models.CharField()

	phone = models.CharField(_('phone'), unique=True, max_length=15, blank=True, default='')
	USERNAME_FIELD = 'phone'

	last_name = models.CharField(_('last name'), max_length=20, blank=True, default='')
	first_name = models.CharField(_('first name'), max_length=20, blank=True, default='')

	owned_flashcards = models.ManyToManyField(Flashcard, through='Ownership')
	date_joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'User: {self.last_name + self.first_name}'



class Ownership(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '(' + student + ',' + flashcard + ')'






# Create your models here.

















