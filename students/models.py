# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    st_birth = models.CharField(blank=True,max_length=128)
    sic_number = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    group_number = models.ForeignKey('Group')
    def __unicode__(self):
        return '%s %s. %s.' % (self.first_name, self.last_name, self.patronymic)


class Group(models.Model):
    group = models.CharField(max_length=128)
    leader = models.ForeignKey('Student')
    def __unicode__(self):
      return self.group


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username
