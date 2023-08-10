from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import UserRequest, UserForm
from hashlib import md5
from datetime import datetime

# Create your views here.
def check_user(username):
    userList = UserRequest.objects.filter(username=username)
    for user in userList:
        if user.status == "Rejected":
            return False
        else:
            return True

def request(request):
    if request.POST:
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            if check_user(userForm.cleaned_data["username"]) is False:
                context = { "form": UserForm(), "status": "rejected_prior" }
                return HttpResponse(template.render(context, request))
            
            user = UserRequest(
                date_created=str(datetime.now()),
                first_name = userForm.cleaned_data["first_name"],
                discord = userForm.cleaned_data["discord"],
                username = userForm.cleaned_data["username"],
                platform = userForm.cleaned_data["platform"],
                status = "Applied",
                reason = None
            )
            user.save()
            if user.pk:
                template = loader.get_template("sent.html")
                return HttpResponse(template.render({}, request))
            else:
                context = { "form": UserForm(), "status": "failed" }
        else:
            context = { "form": UserForm(), "status": "invalid" }
    else:
        context = { "form": UserForm() }
    template = loader.get_template("request.html")
    return HttpResponse(template.render(context, request))