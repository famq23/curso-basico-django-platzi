from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


""" def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        # * La variable ahora está disponible en index.html
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {
        "question": question
    })


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        "question": question
    }) """


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        "Return the last five published questions"
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that are not published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(DetailView):
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "¡No elegiste una respuesta! 😕"
        })
    else:  # * Si todo salió bien entonces haz este bloque
        selected_choice.votes += 1
        selected_choice.save()
        # ! Es buena práctica hacer redirect después de que el usuario usó un formulario
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
