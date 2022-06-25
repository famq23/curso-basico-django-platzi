from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You are in the index page from Premios Platzi App")


def detail(request, question_id):
    return HttpResponse(f'You are watching the question # {question_id}')


def results(request, question_id):
    return HttpResponse(f'You are watching the results from the question # {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting to the question # {question_id}')
