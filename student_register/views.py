from contextlib import contextmanager
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm


def index(request):
    students  = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student_register/index.html', context)



def student_add_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        if request.name == "add":
            form = StudentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("list")
        else:
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect("list")
    context = {
        "form" : form
    }
    return render(request, "student_register/student_form.html", context)














def student_delete(request, id):
    student = Student.objects.get(id=id)
    
    if request.method == "POST":
        student.delete()
        return redirect("list")
    
    context = {
        "student" : student
    }
    
    return render(request, "student_register/student_delete.html", context)
