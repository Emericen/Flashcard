from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from flashcards.models import Collection







class Invitation(models.Model):
	invitation_code = models.CharField(_('invitation_code'), unique=True, max_length=4, blank=True, default='')
	last_name = models.CharField(_('last name'), max_length=10, blank=True, default='')
	first_name = models.CharField(_('first name'), max_length=10, blank=True, default='')
	def __str__(self):
		return f'#{self.invitation_code} for {self.last_name} {self.first_name}'





class UserManager(BaseUserManager):
	def create_user(self, invitation_code, password=None):
		if not invitation_code:
			raise ValueError('Users must have an invitation code')
		new_user = self.model(invitation_code=invitation_code)
		new_user.set_password(password)
		new_user.save()
		return new_user

	def create_staff(self, invitation_code, password=None):
		staff = self.create_user(invitation_code, password=password)
		staff.is_staff = True
		staff.save()
		return admin


	def create_superuser(self, invitation_code, password=None):
		admin = self.create_user(invitation_code, password=password)
		admin.is_superuser = True
		admin.is_staff = True
		admin.save()
		return admin





class User(AbstractBaseUser, PermissionsMixin):
	# user_type = models.CharField()
	objects = UserManager()
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	invitation_code = models.CharField(_('invitation_code'), unique=True, max_length=5, blank=True, default='')
	USERNAME_FIELD = 'invitation_code'

	last_name = models.CharField(_('last name'), max_length=10, blank=True, default='')
	first_name = models.CharField(_('first name'), max_length=10, blank=True, default='')

	owned_collections = models.ManyToManyField(Collection, through='Ownership')
	date_joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.invitation_code}'





class Ownership(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	# flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
	collection = models.ForeignKey(Collection, default=None, on_delete=models.CASCADE)
	date_added = models.DateTimeField(default=timezone.now)

	current_index = models.IntegerField(default=0)


	def __str__(self):
		return '(' + str(self.user) + ', ' + str(self.collection) + ')'















