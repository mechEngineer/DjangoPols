from django.shortcuts import render
from django.http import Http404
from django.template import loader
from .models import Question

# Create your views here.


def index(request):
    # return HttpResponse("<h1> Hello World </h1>")
    latest_q = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_q': latest_q}
    return render(request, 'polls/index.html', context)
# Detail view


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist!')
    return render(request, 'polls/detail.html',  {'question': question})

# Result view


def result(request, question_id):
    response = "You are looking at results of question %s."
    return HttpResponse(response % question_id)

# Vote view


def vote(request, question_id):
    return HttpResponse("You are voting on question %s !" % question_id)
