from django.contrib import admin
from students.models import Group, Student


class StudentInline(admin.TabularInline):
    model = Student


class GroupInline(admin.TabularInline):
    model = Group



class GroupAdmin(admin.ModelAdmin):
    list_display = ('group', 'leader')
    fields = ('group', 'leader')
    inlines = [StudentInline, ]



class StudentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'patronymic',)
    inlines = [GroupInline, ]


admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)

