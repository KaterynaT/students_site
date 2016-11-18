from django.test import TestCase
from students.models import Student


class Create_Group_Test(TestCase):
    def setUp(self):
        Student.objects.create(group='group 3', leader='John Clark. Robert.')

