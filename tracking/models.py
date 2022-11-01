from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)
class Data(models.Model):
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default='M')
    head_circumference = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.email
