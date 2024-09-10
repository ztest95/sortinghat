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
    
    def serialize(self):
        return {
            "name": self.name,
            "uuid": self.uuid
        }
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.uuid
        super().save(*args, **kwargs)
    
class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['name']


class NameLink(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    name = models.ForeignKey('sortinghat.Name', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.link.name} - {self.link.uuid}"
    
    def serialize(self):
        houses = {
            'G': 'Gryffindor',
            'H': 'Hufflepuff',
            'R': 'Ravenclaw',
            'S': 'Slytherin'
        }
        return {
            "name": self.name.name,
            "id": self.name.id,
            "house": houses[self.name.house]
        }