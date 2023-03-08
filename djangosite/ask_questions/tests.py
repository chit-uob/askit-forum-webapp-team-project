import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question, Module


class QuestionModelTests(TestCase):

    def example_test(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        title1 = "testing"
        module = "OSSP"
        m = Module(title=module)
        q = Question(module=m, title=title1)
        self.assertIs(q.title, title1)