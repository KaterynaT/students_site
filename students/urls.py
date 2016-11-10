from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^addgroup/$', views.addgroup, name='addgroup'),
        url(r'^student/$', views.student, name='addstudent'),
        url(r'^(?P<group_number>[0-9]+)/$', views.group, name='group'),
        url(r'^student/(?P<pk>[0-9]+)$', views.student, name='editstudent'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^restricted/', views.restricted, name='restricted'),

]
