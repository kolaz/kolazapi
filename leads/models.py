from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Lead(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'))
    message = models.CharField(_('Message'), max_length=300)
    created_at = models.DateTimeField(_('Craeted at'), auto_now_add=True)