from datetime import datetime
from enum import unique
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.forms import ChoiceField
import datetime


# Create your models here.
class ArticlePage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=255, help_text=("Required. Must be unique."), primary_key =True, error_messages={"unique":"Article with this Title already exists."})
    content = models.TextField(help_text = ('Write content here'))

class ArticleForm(ModelForm):
    class Meta:
        model = ArticlePage
        fields = ['title', 'content']
        help_text = {'content': 'Write content here'}