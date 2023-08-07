from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import UserRequest, UserForm
from hashlib import md5
from datetime import datetime

# Create your views here.

def request(request):
    if request.POST:
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            user = UserRequest(
                date_created=str(datetime.now()),
                first_name = userForm.cleaned_data["first_name"],
                discord = userForm.cleaned_data["discord"],
                username = userForm.cleaned_data["username"],
                platform = userForm.cleaned_data["platform"]
            )
            user.save()
            if user.pk:
                template = loader.get_template("sent.html")
                return HttpResponse(template.render({}, request))
        
    context = { "form": UserForm() }
    template = loader.get_template("request.html")
    return HttpResponse(template.render(context, request))