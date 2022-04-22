from django.shortcuts import render
from sever.models import student, raw_reading, event_table
# Create your views here.
from django.http import HttpResponse


def index(request):
    stu = student.objects.all()
    print(stu[0].name)
    return render(request, 'student.html',{'students':stu })



def engaged(request):
    stu = request.GET['stu']
    print("student name from sever: ",stu)
    student_1 = student.objects.filter(id =stu)
    #print("studnet status:"+ student_1[0].engagement)
    return HttpResponse(student_1[0].engagement)

#   return HttpResponse("Hello,"+ stu[0].name )
