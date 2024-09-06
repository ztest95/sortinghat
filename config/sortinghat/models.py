import random
from django.db import models

from authz.models import User

# Create your models here.

class Name(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}: {self.name} is in {self.house} house"
    
    def serialize(self):
        return {
            "user": self.user.username,
            "name": self.name,
            "house": self.house
        }