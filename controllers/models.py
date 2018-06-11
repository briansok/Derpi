from __future__ import unicode_literals

from django import forms
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
import uuid

class Controllers(models.Model):
    title = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Controller'
        verbose_name_plural = 'Controllers'
        ordering = ['-created']

