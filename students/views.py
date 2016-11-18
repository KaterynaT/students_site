# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from students.forms import AddGroupForm, AddStudentForm, UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from students.models import Group, Student, Info_About_Models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver
from datetime import datetime


def index(request):

    counted_group = Student.objects.values('group_name_id').annotate(Count("id"))
    final_data = []
    for counted_obj in counted_group:
        leader_fmt = {}
        group_obj = Group.objects.filter(id=counted_obj['group_name_id'])
        leader_id = group_obj[0].leader_id
        leader_obj = Student.objects.get(pk=leader_id)
        first_name = leader_obj.first_name
        leader_fmt['people_number'] = counted_obj['id__count']
        leader_fmt['group_name'] = group_obj[0].group
        leader_fmt['leader_name'] = first_name
        final_data.append(leader_fmt)

    return render (request, 'students/index.html', {'final_data': final_data})


def group(request,group_name):
    a = Group.objects.get(group=group_name).pk
    query_results = Student.objects.filter(group_name= a).values()
    pictures = Student.objects.all()
    return render(request,'students/group.html',
                              {'group_name': group_name, 'query_results': query_results, 'pictures': pictures}
                              )


def addgroup(request):
    if request.method == 'POST':
        add_gform = AddGroupForm(data=request.POST)
        add_gform.save()
        return redirect(reverse('index'))

    else:
        add_gform = AddGroupForm()
    return render(request, 'students/addgroup.html', {'add_gform': add_gform})


def edit_student(request, pk=None):
    if request.POST:

        edit_form = AddStudentForm(request.POST, request.FILES)

        if edit_form.is_valid():
            student = Student.objects.get(pk=pk)
            edit_form = AddStudentForm(request.POST, instance=student)
            edit = edit_form.save()
            edit.picture = request.FILES['picture']
            edit.save()

            return redirect(reverse('index'))

        else:
            student = Student.objects.get(pk=pk)
            edit_form = AddStudentForm(instance=student)
            student_edit = Student.objects.get(id=pk)
    else:
        student = get_object_or_404(Student, pk=pk)
        student_edit = Student.objects.get(id=pk)
        edit_form = AddStudentForm(instance=student)
    return render(request, 'students/editstudent.html', {'form': edit_form, 'pk': pk, 'student_edit': student_edit})


def add_student(request):
        if request.POST:
            add_sform = AddStudentForm(data=request.POST)
            add = add_sform.save()
            add.picture = request.FILES['picture']
            add.save()
            return redirect(reverse('index'))
        else:
            add_sform = AddStudentForm()

        return render(request, 'students/addstudent.html', {'add_sform': add_sform})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,
                  'students/register.html',
                  {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/students/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'students/login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/students/')


@receiver(post_save, sender = Student) # редактирование записи (модель Students)
def post_save_students(sender, **kwargs):
    i_a_m = Info_About_Models(model_name='Student')
    i_a_m.model_editing = datetime.now()
    i_a_m.save()


@receiver(post_init, sender = Student) # создание новой записи (модель Students)
def post_init_students(sender, **kwargs):
    i_a_m=Info_About_Models(model_name='Student')
    i_a_m.model_create=datetime.now()
    i_a_m.save()


@receiver(post_delete, sender = Student) #  удаление записи (модель Students)
def post_delete_students(instance, **kwargs):
    i_a_m=Info_About_Models(model_name='Student')
    i_a_m.model_delete=datetime.now()
    i_a_m.save()


@receiver(post_init, sender = Group) # создание новой записи (модель Groups)
def post_init_groups(sender, **kwargs):
    i_a_m=Info_About_Models(model_name='Group')
    i_a_m.model_create=datetime.now()
    i_a_m.save()


@receiver(post_save, sender = Group) # редактирование записи (модель Groups)
def post_save_groups(sender, **kwargs):
    i_a_m=Info_About_Models(model_name='Group')
    i_a_m.model_editing=datetime.now()
    i_a_m.save()


@receiver(post_delete, sender = Group) # удаление записи (модель Groups)
def post_delete_groups(sender, **kwargs):
    i_a_m=Info_About_Models(model_name='Group')
    i_a_m.model_delete=datetime.now()
    i_a_m.save()
