from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from django.shortcuts  import redirect
from .models import Student
from django.shortcuts import get_object_or_404, redirect, render

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            form = StudentForm()
        return render(request, 'create.html', {'form':form})
    
    form = StudentForm()
    return render(request, 'create.html', {'form':form})


def student_list(request):
    student = Student.objects.all()
    return render(request, 'list.html', {'students':student})


def update_student(request, primarykey):
    student = get_object_or_404(Student, id=primarykey)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = StudentForm(instance=student)  # ← this is crucial

    return render(request, 'update.html', {'form': form})

def delete_student(request, primarykey):
    student = get_object_or_404(Student, id=primarykey)

    if request.method == "POST":
        student.delete()
        return redirect('list')

    return render(request, 'delete_confirm.html', {'student': student})
