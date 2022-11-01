import datetime
from django.contrib.auth.models import User
from django.db import models

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    is_thread = models.BooleanField(default=False)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    replies = models.IntegerField(default=0)