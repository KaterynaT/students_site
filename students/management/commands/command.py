from django.core.management.base import BaseCommand
from students.models import Group, Student


class Command(BaseCommand):

    def handle(self, **options):
        group_all = list(Group.objects.all())
        for i in Student.objects.all():
            print i.first_name



        print group_all
