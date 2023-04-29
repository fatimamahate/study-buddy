from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment
from .forms import AssignmentForm
from django.contrib.auth.models import User

# Create your views here.


def dashboard(request):
    assignment = Assignment.objects.all()
    context = {'assignment': assignment}
    return render(request, 'study/dashboard.html', context)


def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = AssignmentForm()
    context = {
        'form': form
    }
    return render(request, 'study/add_assignment.html', context)


def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.user != assignment.tutor:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = AssignmentForm()
    context = {
        'form': form
    }
    return render(request, 'study/edit_assignment.html', context)

