from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from summaryze.models import Summary


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_summarize_view_get(self):
        response = self.client.get(reverse('summarize'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'file_upload.html')

    def test_summarize_view_post(self):
        with open('test_document.txt', 'w') as f:
            f.write('Test document content')

        with open('test_document.txt', 'rb') as document:
            response = self.client.post(reverse('summarize'), {'document': document})

        self.assertEqual(response.status_code, 302)  # Should redirect to summary view

    def test_summary_view(self):
        summary = Summary.objects.create(original_text='Original Text', summary_text='Summary Text', user_id=self.user)
        response = self.client.get(reverse('summary', args=[summary.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'summary.html')
