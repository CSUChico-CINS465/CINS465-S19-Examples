from django.test import TestCase

# Create your tests here.
from .models import Suggestion

# Create your tests here.
class SuggestionTestCase(TestCase):
    def setUp(self):
        Suggestion.objects.create(suggestion_field="lion")
        Suggestion.objects.create(suggestion_field="cat")

    def test_suggestion_to_string(self):
        lion = Suggestion.objects.get(suggestion_field="lion")
        cat = Suggestion.objects.get(suggestion_field="cat")
        self.assertEqual(str(lion), 'lion')
        self.assertEqual(str(cat), 'cat')
