from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Attribute(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100, blank=True, default='')
  category = models.CharField(max_length=100, blank=True, default='')
  class Meta:
      ordering = ('created',)

class College(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100, blank=True, default='')
  size = models.CommaSeparatedIntegerField(max_length=9999999999999)
  owner = models.ForeignKey('auth.User', related_name='colleges')
  attributes = models.ManyToManyField(Attribute, blank=True)
  class Meta:
      ordering = ('created',)

class Student(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100, blank=True, default='')
  # user = models.OneToOneField(User)
  college_list = models.ManyToManyField(College, blank=True)
  class Meta:
      ordering = ('created',)

# class CollegeAttribute(models.Model):
#   added = models.DateTimeField(auto_now_add=True)
#   college = models.ForeignKey('College')
#   attribute = models.ForeignKey('Attribute')
#   class Meta:
#       ordering = ('added',)


