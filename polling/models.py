"""
This new model represented a new table that I wanted stored in my database,
so I had to migrate this new table into the existing database:
"""

from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title