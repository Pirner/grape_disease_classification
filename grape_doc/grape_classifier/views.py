from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import ClassificationRequestForm


# Create your views here.
def index(request):
    template = loader.get_template('grape_classifier/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the polls index.")


def classify_view(request):
    template = loader.get_template('grape_classifier/classify_view.html')
    context = {}

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClassificationRequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # TODO work on when a form is valid
            return HttpResponse(template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClassificationRequestForm()
        print('requested the classification view in GET?')

    context = {'form': form}
    return HttpResponse(template.render(context, request))
    # return render(request, 'name.html', {'form': form})


def detail(request, grape_classification_id):
    return HttpResponse("You're looking at question %s." % grape_classification_id)
