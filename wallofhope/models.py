from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class wallofhope(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    judul = models.CharField(max_length=80, null = True)
    deskripsi = models.TextField(max_length = 200)
    image = models.URLField(max_length=200, null = True)