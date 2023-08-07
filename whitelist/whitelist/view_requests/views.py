from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from whitelist.requests.models import UserRequest
# Create your views here.

def view_requests(request):
    if request.POST:
        print(request.POST)
    template = loader.get_template("view_requests.html")
    forms = UserRequest.objects.all()
    context = {"forms": forms}
    return HttpResponse(template.render(context, request))