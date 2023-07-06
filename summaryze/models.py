from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Summary(models.Model):
    """A single summary entry database model"""

    original_text = models.TextField()
    summary_text = models.TextField()
    num_paragraphs = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='summaries')

    def get_absolute_url(self):
        """Return URL for each summary page"""
        return reverse("summary", args=[str(self.pk)])
