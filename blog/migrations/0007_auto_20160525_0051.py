# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pystagram.validators
import pystagram.file


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=pystagram.file.random_name_with_file_field, blank=True, validators=[pystagram.validators.jpeg_validator], null=True),
        ),
    ]
