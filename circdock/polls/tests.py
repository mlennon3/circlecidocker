import datetime
from django.test import TestCase
from django.utils import timezone
from polls.models import Question

class FooTest(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 3)
        self.assertEqual(5 + 5, 10)

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_writing_to_db(self):
        time = timezone.now() + datetime.timedelta(days=30)
        Question.objects.create(question_text='Why', pub_date=time)
        self.assertTrue(len(Question.objects.all()) > 0)
