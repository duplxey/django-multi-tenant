from django.db import models

from core.models import TimeStampedModel


class Article(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"
