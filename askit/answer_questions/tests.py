from django.test import TestCase
from django.contrib.auth.models import User
from home_page.models import Question, Answer, Tag, Module, Comment
from .views import check_upvote_or_downvote_question, check_upvote_or_downvote_answer

# Create your tests here.

class AnswerQuestionsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()
        self.module = Module.objects.create(title='test module', description='test description')
        self.module.save()
        self.question = Question.objects.create(author=self.user, module=self.module, title='test question', explanation='test explanation', tried_what='test tried_what', summary='test summary')
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