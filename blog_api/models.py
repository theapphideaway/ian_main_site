from django.db import models


class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateField()
    content = models.JSONField()
