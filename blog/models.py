from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from uuid import uuid4
from pystagram.validators import jpeg_validator
from pystagram.image import receiver_with_image_field
from pystagram.file import random_name_with_file_field


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    uuid = models.UUIDField(default=uuid4, editable=False, db_index=True)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True, validators=[jpeg_validator],
                              upload_to=random_name_with_file_field)
    lnglat = models.CharField(max_length=100, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    origin_url = models.URLField(blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.uuid.hex])

    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1]

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]

    @classmethod
    def timeline(cls, from_user):
        following_users = [follow.to_user_id for follow in from_user.following_set.all()]
        return cls.objects.filter(Q(author=from_user) | Q(author__in=following_users))

receiver = receiver_with_image_field('photo', 1024)
pre_save.connect(receiver, sender=Post)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
