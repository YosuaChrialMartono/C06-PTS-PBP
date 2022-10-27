from datetime import datetime
from enum import unique
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
import datetime

capitalizeFirstChar = lambda s: s[:1].upper() + s[1:]
# Create your models here.
class ArticlePage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()

class ArticleForm(ModelForm):
    class Meta:
        model = ArticlePage
        fields = ['title', 'content']
        help_text = {'description': 'Write task description'}