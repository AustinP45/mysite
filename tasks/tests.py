from django.test import TestCase
from django.test import Client

class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
		  """
        If no tasks exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks are available.")
        self.assertQuerysetEqual(response.context['todo_list'], [])
