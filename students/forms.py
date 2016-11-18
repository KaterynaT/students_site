# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from students.models import Student, Group


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group','leader')


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('id',
                  'first_name',
                  'last_name',
                  'patronymic',
                  'birth',
                  'sic_number',
                  'group_name',
                  'picture')

