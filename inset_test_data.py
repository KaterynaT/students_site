from students.models import Student, Group
from django.db.models import Count

counted_group = Student.objects.values('group_number_id').annotate(Count("id"))
print(counted_group)
final_data = []
for counted_obj in counted_group:
    leader_fmt = {}
    leaders = Group.objects.get(id=counted_obj['group_number_id'])
    leader_fmt['people_number'] = counted_obj['id__count']
    leader_fmt['group_number'] = leaders.group
    leader_fmt['leader_name'] = leaders.leader
    final_data.append(leader_fmt)

print(final_data)
