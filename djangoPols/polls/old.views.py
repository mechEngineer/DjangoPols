from django.shortcuts import render, get_object_or_404, reverse
from django.http import Http404, HttpResponseRedirect
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})
# Vote view


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question coting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Alway return HttpResponseRedirect after successfully dealling with POST data.
        # This prevents data from being posted twice if a user hits the Back Button
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
