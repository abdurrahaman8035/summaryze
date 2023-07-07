from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from summaryze.models import Summary


class SummaryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.summary = Summary.objects.create(
            original_text='Original Text',
            summary_text='Summary Text',
            document='test_document.txt',
            user_id=self.user
        )

    def test_summary_absolute_url(self):
        expected_url = reverse('summary', args=[str(self.summary.pk)])
        self.assertEqual(self.summary.get_absolute_url(), expected_url)
