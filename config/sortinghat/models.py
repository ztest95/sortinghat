import random
from django.db import models

from django.forms import ModelForm
from authz.models import User

# Create your models here.

class Name(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    CHOICES = (
        ('G', 'Gryffindor'),
        ('H', 'Hufflepuff'),
        ('R', 'Ravenclaw'),
        ('S', 'Slytherin')
    )
    house = models.CharField(max_length=1, choices=CHOICES, blank=False)

    def save (self, *args, **kwargs):
        if not self.house:
            self.house = random.choice([choice[0] for choice in self.CHOICES])

        self.name = self.name.lower()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.get_house_display()}"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "house": self.house
        }

class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ['name', 'house']