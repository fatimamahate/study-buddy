from django.shortcuts import render, HttpResponse

# Create your views here.


def test_response(request):
    return HttpResponse("HeY!")
