from django.db import models
from django.forms import ModelForm
from datetime import datetime
# Create your models here.

class UserRequest(models.Model):

    platform_list = [
        ("J", "Java Edition"),
        ("B", "Bedrock Edition"),
    ]

    first_name     =  models.CharField(max_length=20)
    date_created   =  models.CharField(max_length=32, primary_key=True)
    discord        =  models.CharField(max_length=30)
    username       =  models.CharField(max_length=30)
    platform       =  models.CharField(max_length=1, choices=platform_list)
    status         =  models.CharField(max_length=15, default="Applied")
    reason         =  models.CharField(max_length=100, null=True)

    def __str__(self):
        if self.status == "Rejected":
            return f"{self.username}: {self.status}"
        return f"{self.username}: {self.status}"
    
class UserForm(ModelForm):
    class Meta:
        model = UserRequest
        fields = ["first_name", "discord", "username", "platform"]