from django.db import models

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
    def __str__(self):
        return self.username