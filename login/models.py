from secrets import choice
from site import USER_BASE
from unittest import result
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class Stunting(BaseUserManager):
    def create_user(self, email, username, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_subscribed = True
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    class Role(models.TextChoices):
        PENGUNJUNG = "PENGUNJUNG", 'Pengunjung'
        DOKTER = "DOKTER", 'Dokter'
        PASIEN = "PASIEN", 'Pasien'
    
    base_role = Role.PENGUNJUNG 
    role = models.CharField(max_length=50, choices=Role.choices, null=True)
    
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    username = models.CharField(max_length=30, unique=True, default=None)
    nama = models.CharField(max_length=100)
    is_subscribed = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = Stunting()
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
class DokterManager(BaseUserManager):
    def get_queryset (self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.DOKTER)
    
class Dokter (User):
    base_role = User.Role.DOKTER
    dokter = DokterManager()
    class Meta:
        proxy = True
    
    def welcome(self):
        return "Hanya untuk akses dokter"
    
@receiver(post_save, sender=Dokter)
def create_user_profile (sender, instance, created, **kwargs):
    if created and instance.role == "DOKTER":
        DokterProfile.objects.create(user=instance)

class DokterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dokter_id = models.IntegerField(null=True, blank=True)
    
class PasienManager(BaseUserManager):
    def get_queryset (self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.PASIEN)
    
class Pasien (User):
    base_role = User.Role.PASIEN
    pasien = PasienManager()
    class Meta:
        proxy = True
    
    def welcome(self):
        return "Hanya untuk akses pasien"
    
@receiver(post_save, sender=Pasien)
def create_user_profile (sender, instance, created, **kwargs):
    if created and instance.role == "PASIEN":
        PasienProfile.objects.create(user=instance)
    
class PasienProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pasien_id = models.IntegerField(null=True, blank=True)

