# Generated by Django 3.2.7 on 2021-09-03 04:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Game',
            new_name='Games',
        ),
    ]
