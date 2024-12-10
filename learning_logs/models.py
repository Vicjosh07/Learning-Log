from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    # Many-to-one relationship will be built.
    # Many entries to one entry

    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something specific learned about the topic """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # Foreign Key as a database term...another record in the database
    # Each topic creates an ID in the Database
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string rep of the entry"""
        # return f'{self.text[:50]}....'
        if len(self.text[:]) >= 50:
            return f'{self.text[:50]}....'
        return self.text
