from django.shortcuts import render

# Create your views here.


def get_assignment_list(request):
    return render(request, 'study/dashboard.html')
