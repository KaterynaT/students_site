# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from students.models import Student, Group, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group','leader')


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'st_birth','sic_number', 'group_number', 'picture')


