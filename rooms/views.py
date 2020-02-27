from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from . import models


def all_rooms(request):
    # check specifics of request
    # print(dir(request))

    # now = datetime.now()
    # hungry = True
    # return HttpResponse(content=f"hello {now}")

    # render is telling Django "go and compile html code into browser html"
    # context is way of sending variables to html file, as {{variable}}. Logic statements go into {% if %}
    # return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})

    all_rooms = models.Room.objects.all()
    return render(request, "rooms/all_rooms.html", context={"rooms_display": all_rooms})

