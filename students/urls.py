from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addgroup/$', views.addgroup, name='addgroup'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^student/$', views.add_student, name='addstudent'),
    url(r'^student/(?P<pk>[0-9]+)$', views.edit_student, name='editstudent'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^(?P<group_name>[0-9a-zA-Z]+)/$', views.group, name='group'),
]
