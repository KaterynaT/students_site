# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from students.forms import AddGroupForm, AddStudentForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from students.models import Group, Student
from django.core.urlresolvers import reverse


def index(request):

    counted_group = Student.objects.values('group_number_id').annotate(Count("id"))
    final_data = []
    for counted_obj in counted_group:
        leader_fmt = {}
        group_obj = Group.objects.filter(id=counted_obj['group_number_id'])
        leader_id = group_obj[0].leader_id
        leader_obj = Student.objects.get(pk=leader_id)
        first_name = leader_obj.first_name
        leader_fmt['people_number'] = counted_obj['id__count']
        leader_fmt['group_number'] = group_obj[0].group
        leader_fmt['leader_name'] = first_name
        final_data.append(leader_fmt)


    return render (request, 'students/index.html',
        {'final_data': final_data}
                   )

def group(request,group_number):
    a = Group.objects.get(group=group_number).pk
    query_results = Student.objects.filter(group_number= a).values()
    pictures = Student.objects.all()
    return render(request,'students/group.html',
                              {'query_results': query_results, 'pictures': pictures}
                              )


def addgroup(request):
    if request.method == 'POST':
        add_gform = AddGroupForm(data=request.POST)
        add_gform.save()
        return redirect(reverse('index'))

    else:
        add_gform = AddGroupForm()
    return render(request,
                  'students/addgroup.html',
                  {'add_gform': add_gform}
                  )

def student(request, pk=None):
    if pk:
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
        else:
            student = get_object_or_404(Student, pk=pk)
            edit_form = AddStudentForm(instance=student)
        return render(request, 'students/editstudent.html', {'form': edit_form, 'pk': pk})
    else:
        if request.method == 'POST':
            add_sform = AddStudentForm(data=request.POST)
            add = add_sform.save()
            add.picture = request.FILES['picture']
            add.save()
            return redirect(reverse('index'))

        else:
            add_sform = AddStudentForm()

        return render(request,
                      'students/addstudent.html',
                      {'add_sform': add_sform}
                      )



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'students/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


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

