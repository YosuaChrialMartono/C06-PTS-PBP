from datetime import datetime
from enum import unique
from django.db import models
from django.forms import ModelForm
import datetime
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.
class ArticlesPage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=255, help_text=("Required. Must be unique. Letters and digit only with fewer than 150 word."), primary_key =True, error_messages={"unique":"Article with this Title already exists."})
    content = models.TextField(help_text = ('Write content here'))

class ArticleForm(ModelForm):
    class Meta:
        model = ArticlesPage
        fields = ['title', 'content']
        help_text = {'content': 'Write content here'}