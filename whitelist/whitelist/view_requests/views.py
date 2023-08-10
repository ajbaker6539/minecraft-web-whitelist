from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from whitelist.requests.models import UserRequest
# Create your views here.

def view_requests(request):
    template = loader.get_template("view_requests.html")
    forms = UserRequest.objects.filter(status="Applied")

    if request.POST:
        user = UserRequest.objects.get(date_created=request.POST["date_created"])
        if request.POST["option"] == "accept":
            user.status = "Accepted"
            user.save()
            username = user.username
            context = {"forms": forms, "status": "accepted", "name": username}
        elif request.POST["option"] == "reject":
            user.status = "Rejected"
            if request.POST["reason"]:
                user.reason = request.POST["reason"]
                print("POST!")
            user.save()
            username = user.username
            context = {"forms": forms, "status": "rejected", "name": username}
    else:
        context = {"forms": forms, "status": "none"}
    return HttpResponse(template.render(context, request))