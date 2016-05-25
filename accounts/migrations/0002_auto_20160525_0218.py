# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='following_set')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='follower_set')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userfollow',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
