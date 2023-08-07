from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from whitelist.requests.models import UserRequest
# Create your views here.

def view_requests(request):
    template = loader.get_template("view_requests.html")
    forms = UserRequest.objects.filter(accepted="False")

    if request.POST:
        user = UserRequest.objects.get(date_created=request.POST["date_created"])
        user.accepted = True
        user.save()
        context = {"forms": forms, "accepted_name": user.username}
    else:
        context = {"forms": forms}
    return HttpResponse(template.render(context, request))