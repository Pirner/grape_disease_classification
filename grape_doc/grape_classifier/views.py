from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('grape_classifier/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, grape_classification_id):
    return HttpResponse("You're looking at question %s." % grape_classification_id)
