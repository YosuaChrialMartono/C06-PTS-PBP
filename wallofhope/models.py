from django.db import models

class wallofhope(models.Model):
    judul = models.CharField(max_length=80, null = True)
    deskripsi = models.TextField(max_length = 200)
    image = models.ImageField(upload_to= "wallofhope/image")