from __future__ import unicode_literals

from django import forms
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User

class Categories(models.Model):
    title = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name='categories')
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created']
