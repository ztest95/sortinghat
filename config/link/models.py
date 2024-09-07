import uuid

from django.forms import ModelForm
from django.db import models

# Create your models here.

class Link(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('authz.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, blank=False)

    def __str__(self):
        return f"{self.name} - {self.uuid}"
    
class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['name']

