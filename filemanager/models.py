from enum import unique
from os import access
from unicodedata import category
from django.db import models
import django
import datetime
import secrets
from django.contrib.auth.models import AbstractUser, Group, Permission
from sqlalchemy import null


# Create your models here.
class Department(models.Model):
	name= models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

class Employee(AbstractUser):
	phone_no = models.CharField(max_length=10, null=True, blank=True)
	department = models.ForeignKey(Department, related_name='employees',on_delete=models.DO_NOTHING, blank=True, null=True)
	groups = models.ManyToManyField(Group)
	user_permissions = models.ManyToManyField(Permission)

class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField()

class Access(models.Model):
    status = models.CharField(max_length=10, unique=True)

class File(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    file_location = models.FileField(upload_to='myfiles', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='files', on_delete=models.DO_NOTHING, blank=True, null=True)
    added_by = models.ForeignKey(Employee, related_name='files', on_delete=models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Department, related_name='files', on_delete=models.DO_NOTHING, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    shared_to = models.ManyToManyField(Employee, through='FileShare')

    def __str__(self):
        return self.name

class FileShare(models.Model):
    file = models.ForeignKey(File, related_name='fileshares', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(Employee, related_name='fileshares', on_delete=models.DO_NOTHING)
    access = models.ForeignKey(Access, related_name='files', on_delete=models.DO_NOTHING, blank=True, null=True)       
    date_shared = models.DateTimeField(auto_now_add=True)