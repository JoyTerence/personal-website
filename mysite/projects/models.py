from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.TextField()
    def __unicode__(self):
        return self.title
