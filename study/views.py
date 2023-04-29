from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from .subjects import SubjectForm

# Create your views here.


def get_assignment_list(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'study/dashboard.html', context)


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_assignment_list')
    form = SubjectForm()
    context = {
        'form': form
    }
    return render(request, 'study/add_subject.html', context)


def edit_subject(request, subject_id):
    subject=get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('get_assignment_list')
    form = SubjectForm()
    context = {
        'form': form
    }
    return render(request, 'study/edit_subject.html', context)

