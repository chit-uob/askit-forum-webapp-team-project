import datetime

from django.test import TestCase
from django.utils import timezone

from home_page.models import Question, Module


class QuestionModelTests(TestCase):

    def test_example_test(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        title1 = "testing"
        module = "OSSP"
        m = Module(title=module)
        q = Question(module=m, title=title1)
        self.assertIs(q.title, title1)