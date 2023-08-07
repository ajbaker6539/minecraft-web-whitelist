from django.db import models
from django.forms import ModelForm
# Create your models here.

class User(models.Model):

    platform_list = [
        ("W", "Windows"),
        ("M", "MacOS"),
        ("L", "Linux"),
        ("X", "XBOX"),
        ("P", "Playstation"),
        ("S", "Switch"),
        ("I", "iOS"),
        ("A", "Android"),
    ]

    first_name = models.CharField(max_length=20)
    discord = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    platform = models.CharField(max_length=1, choices=platform_list)
    accepted = False

    def __str__(self):
        return self.username
    
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "discord", "username", "platform"]