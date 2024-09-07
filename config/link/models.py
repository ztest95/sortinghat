import uuid

from django.db import models

# Create your models here.

class Link(models.Model):
    user = models.ForeignKey('authz.User', on_delete=models.CASCADE)
    link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, blank=False)

