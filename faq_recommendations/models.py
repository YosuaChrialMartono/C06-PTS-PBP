from django.db import models

# Create your models here.
class FreqAskedQuestions(models.Model):
    title = models.TextField()
    description = models.TextField()