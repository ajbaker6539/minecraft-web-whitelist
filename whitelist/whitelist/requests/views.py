from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import User, UserForm

# Create your views here.

def request(request):
    if request.POST:
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            template = loader.get_template("sent.html")
            return HttpResponse(template.render({}, request))
        
    context = { "form": UserForm() }
    template = loader.get_template("request.html")
    return HttpResponse(template.render(context, request))