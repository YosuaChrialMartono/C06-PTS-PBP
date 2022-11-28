# Generated by Django 4.1 on 2022-11-02 14:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesPage',
            fields=[
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(error_messages={'unique': 'Article with this Title already exists.'}, help_text='Required. Must be unique.', max_length=255, primary_key=True, serialize=False)),
                ('content', models.TextField(help_text='Write content here')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]