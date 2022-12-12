from django.db import models

# Create your models here.
class FreqAskedQuestions(models.Model):
    title = models.TextField()
    description = models.TextField()

class Experiences(models.Model):
    nama = models.TextField()
    email = models.TextField()
    nomorHP = models.TextField()
    message = models.TextField()