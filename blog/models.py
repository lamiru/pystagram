from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from uuid import uuid4
from pystagram.validators import jpeg_validator

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
    photo = models.ImageField(blank=True, null=True, validators=[jpeg_validator])
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
