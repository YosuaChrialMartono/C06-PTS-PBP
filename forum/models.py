import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    is_thread = models.BooleanField(default=False)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    replies = models.IntegerField(default=0)