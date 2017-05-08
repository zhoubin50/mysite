from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_detail = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.blog_title

    def was_published_recently(self):
        now = timezone.now()
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now

