from django.contrib.auth.models import StudentRegistration
users = [str(user) for user in StudentRegistration.objects.all()]
student_list = [()]
for ok in (users):
    student_list.append((ok,ok))
st_lst=student_list[2:]
#print(st_lst)
student_ = tuple(st_lst) 
#print(student_)