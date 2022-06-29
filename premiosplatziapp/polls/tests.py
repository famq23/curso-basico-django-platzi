import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# * Lo más común es hacer tests sobre modelos y/o vistas en Django


class QuestionModelTests(TestCase):
    def setUp(self):
        self.question = Question(
            question_text='¿Quién es el mejor Course Director de Platzi?')
        self.future_time = timezone.now() + datetime.timedelta(days=30)
        self.past_time = timezone.now() - datetime.timedelta(days=30)
        self.recent_time = timezone.now()

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        self.question.pub_date = self.future_time
        self.assertIs(self.question.was_published_recently(), False)

    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns True for questions whose pub_date is in the past"""
        self.question.pub_date = self.past_time
        self.assertIs(self.question.was_published_recently(), False)

    def test_was_published_recently_with_recent_questions(self):
        """was_published_recently returns True for questions whose pub_date is today"""
        self.question.pub_date = self.recent_time
        self.assertIs(self.question.was_published_recently(), True)


class QuestionIndexViewTests(QuestionModelTests, TestCase):
    def test_no_questions(self):
        """If no question exist, an appropiate message is displayed"""
        # * Hago una petición GET al index de polls y guardo la respuesta en response
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_show_only_recent_questions(self):
        """The view should only show recent questions. It cannot show future questions from the date they are consulted."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        future_question = [self.question, self.future_time]
        self.assertNotContains(response, future_question)
