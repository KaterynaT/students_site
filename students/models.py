# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Info_About_Models(models.Model):
    model_name = models.CharField(max_length=255,verbose_name=u'Имя модели')
    model_create = models.CharField(max_length=255,verbose_name=u'Информация о создании новой записи в модель')
    model_editing = models.CharField(max_length=255,verbose_name=u'Информация о редактировании модели')
    model_delete = models.CharField(max_length=255,verbose_name=u'Информация об удалении записи из модели')

    class Meta:
        verbose_name_plural = "Информация о моделях"

    def __unicode__(self):
        return self.model_name


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    birth = models.DateField(null=True, blank=True)
    sic_number = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    group_name = models.ForeignKey('Group')

    def __unicode__(self):
        return '%s %s. %s.' % (self.first_name, self.last_name, self.patronymic)


class Group(models.Model):
    group = models.CharField(max_length=128)
    leader = models.ForeignKey('Student')

    def __unicode__(self):
        return self.group


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username
