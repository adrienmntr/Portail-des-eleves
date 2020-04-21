# Generated by Django 2.2.10 on 2020-04-21 22:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='have_voted',
            field=models.ManyToManyField(blank=True, related_name='course', to=settings.AUTH_USER_MODEL),
        ),
    ]