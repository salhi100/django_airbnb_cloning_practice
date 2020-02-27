from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from . import models


def all_rooms(request):
    # check specifics of request
    # https://docs.djangoproject.com/en/3.0/ref/request-response/#httprequest-objects
    # print(dir(request))

    # print get request
    # print(dir(request.GET))

    # http://127.0.0.1:8000/?page=1
    # print(request.GET.keys())
    page = int(request.GET.get("page", 1))  # page is 1 by default
    page_size = 10
    limit = page * page_size
    offset = limit - page_size

    # accessing database with queryset
    # queryset is lazy. objects.all()[:10] only gets 10 items, not all item and extracting 10 items from it
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#limiting-querysets
    all_rooms = models.Room.objects.all()[offset:limit]

    # render is telling Django "go and compile html code into browser html"
    # context is way of sending variables to html file, as {{variable}}. Logic statements go into {% if %}
    # return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
    return render(request, "rooms/all_rooms.html", context={"rooms_display": all_rooms})

    # now = datetime.now()
    # hungry = True
    # return HttpResponse(content=f"hello {now}")

