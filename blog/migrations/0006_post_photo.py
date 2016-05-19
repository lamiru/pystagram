# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pystagram.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_lnglat'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, blank=True, upload_to='', validators=[pystagram.validators.jpeg_validator]),
        ),
    ]
