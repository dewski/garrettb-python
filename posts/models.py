from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import re

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    user = models.ForeignKey(User)
    categories = models.ManyToManyField('Category')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        if self.updated_at is not None:
            self.updated_at = datetime.now()
        super(Post, self).save()

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    posts = models.ManyToManyField('Post')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        if self.updated_at is not None:
            self.updated_at = datetime.now()
        super(Category, self).save()