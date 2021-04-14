from django.db import models
from .utils import random_key


class ReadedManager(models.Manager):
	def get_queryset(self):
		return super(ReadedManager, self).get_queryset().filter(is_readed=True)


class Contact(models.Model):
	key = models.CharField(default=random_key, unique=True, max_length=13)
	name = models.CharField(max_length=30)
	email = models.EmailField()
	subject = models.CharField(max_length=30, blank=True, null=True)
	text = models.TextField()
	phone_number = models.CharField(max_length=13, blank=True, null=True)
	address = models.CharField(max_length=40, blank=True, null=True)
	datetime = models.DateTimeField(auto_now=True)
	ip = models.GenericIPAddressField(blank=True, null=True)
	is_readed = models.BooleanField(default=False)

	objects = models.Manager()
	readed = ReadedManager()

	def __str__(self):
		return self.name


class MassEmail(models.Model):
	key = models.CharField(default=random_key, max_length=13, unique=True)
	datetime = models.DateTimeField(auto_now=True)
	admin_name = models.CharField(max_length=30, blank=True, null=True)
	subject = models.CharField(max_length=50)
	text = models.TextField()

	def __str__(self):
		return self.name
