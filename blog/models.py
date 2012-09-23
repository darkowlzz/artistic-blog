from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, unique=False)
    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
