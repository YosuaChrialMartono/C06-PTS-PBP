# Generated by Django 4.1 on 2022-11-01 14:06

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_dokter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasien',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('login.user',),
            managers=[
                ('pasien', django.db.models.manager.Manager()),
            ],
        ),
    ]