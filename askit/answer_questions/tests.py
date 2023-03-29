import json

from django.test import TestCase
from django.contrib.auth.models import User
from home_page.models import Question, Answer, Tag, Module, Comment
from .views import check_upvote_or_downvote_question, check_upvote_or_downvote_answer, view_question
from rest_framework.test import APIRequestFactory, force_authenticate


def format_response_date(datetime_object):
    return datetime_object.strftime("%Y-%m-%d") + "T" + datetime_object.strftime("%H:%M:%S.%f")[:-3] + "Z"


# Create your tests here.

class AnswerQuestionsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123456789')
        self.user.save()
        self.module = Module.objects.create(title='testmodule', description='test description')
        self.module.save()
        self.question = Question.objects.create(author=self.user, module=self.module, title='test question',
                                                explanation='test explanation', tried_what='test tried_what',
                                                summary='test summary')
        self.question.save()
        self.answer = Answer.objects.create(author=self.user, question=self.question, content='test content')
        self.answer.save()

    def test_check_upvote_or_downvote_question_not_voted(self):
        self.assertEqual(check_upvote_or_downvote_question(self.question, self.user), "none")

    def test_check_upvote_or_downvote_question_upvoted(self):
        self.question.upvotes.add(self.user)
        self.assertEqual(check_upvote_or_downvote_question(self.question, self.user), "upvote")

    def test_check_upvote_or_downvote_question_downvoted(self):
        self.question.upvotes.remove(self.user)
        self.question.downvotes.add(self.user)
        self.assertEqual(check_upvote_or_downvote_question(self.question, self.user), "downvote")

    def test_check_upvote_or_downvote_answer_not_voted(self):
        self.assertEqual(check_upvote_or_downvote_answer(self.answer, self.user), "none")

    def test_check_upvote_or_downvote_answer_upvoted(self):
        self.answer.upvotes.add(self.user)
        self.assertEqual(check_upvote_or_downvote_answer(self.answer, self.user), "upvote")

    def test_check_upvote_or_downvote_answer_downvoted(self):
        self.answer.upvotes.remove(self.user)
        self.answer.downvotes.add(self.user)
        self.assertEqual(check_upvote_or_downvote_answer(self.answer, self.user), "downvote")

    def test_response_of_view_question(self):
        factory = APIRequestFactory()
        request = factory.get(f'/api/question/{self.question.id}/')
        request.user = self.user
        force_authenticate(request, user=self.user)
        response = view_question(request, self.question.id)
        response_json = json.loads(response.content)
        self.assertEqual(response_json['question_id'], self.question.id)
        expected_response = {"question_id": 1, "title": "test question", "author": "testuser", "module": "testmodule",
                             "explanation": "test explanation", "tried_what": "test tried_what",
                             "summary": "test summary", "pub_date": format_response_date(self.question.pub_date),
                             "status": "Unanswered",
                             "tags": [], "score": 0, "views": 1, "upvote_or_downvote": "none", "comment_list": [],
                             "answer_list": [{"id": 1, "author": "testuser", "content": "test content",
                                              "pub_date": format_response_date(self.answer.pub_date), "score": 0,
                                              "is_solution": False,
                                              "upvote_or_downvote": "none"}]}
        self.assertEqual(response_json, expected_response)
