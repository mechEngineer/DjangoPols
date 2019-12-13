from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1> Hello World </h1>")

# Detail view


def detail(request, question_id):
    return HttpResponse("<p>Wel well well. If it aint invisible cunt</p>")

# Result view


def result(request, question_id):
    response = "You are looking at results of question %s."
    return HttpResponse(response % question_id)

# Vote view


def vote(request, question_id):
    return HttpResponse("You are voting on question %s !" % question_id)
