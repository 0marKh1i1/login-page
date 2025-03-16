from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username:
			raise ValueError('An username is required.')
		if not password:
			raise ValueError('A password is required.')
		username = username.lower() 
		user = self.model(username=username)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self, username, password=None):
		if not username:
			raise ValueError('An username is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(username, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user


class AppUser(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField (max_length=50, unique=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []
	objects = AppUserManager()
	def __str__(self):
		return self.username