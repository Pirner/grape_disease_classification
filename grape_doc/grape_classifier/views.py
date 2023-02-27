from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, grape_classification_id):
    return HttpResponse("You're looking at question %s." % grape_classification_id)
