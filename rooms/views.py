from math import ceil
from django.shortcuts import render

# paginator for django
from django.core.paginator import Paginator
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
    page = request.GET.get("page")  # page is 1 by default

    # queryset of them are ready as list
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#querysets-are-lazy
    room_list = models.Room.objects.all()

    # dictionary with keys of "object_list", "number", "paginator"
    # object_list is list of queryset, number is integer, paginator is class
    # https://docs.djangoproject.com/en/3.0/topics/pagination/
    paginator = Paginator(room_list, 10)
    rooms_pages = paginator.get_page(page)
    # print(vars(rooms_pages))

    # dictionary with keys of 'per_page', 'orphans', 'allow_empty_first_page', 'count', 'num_pages'
    # print(vars(rooms_pages.paginator))
    # https://docs.djangoproject.com/en/3.0/ref/paginator/#django.core.paginator.Paginator
    # total_pages = int(rooms_pages["paginator"]["num_pages"])

    # render is telling Django "go and compile html code into browser html"
    # context is way of sending variables to html file, as {{variable}}. Logic statements go into {% if %}
    # context = {"context name": variableInViews.py}
    return render(
        request, "rooms/all_rooms.html", context={"rooms_pages": rooms_pages},
    )

    # now = datetime.now()
    # hungry = True
    # return HttpResponse(content=f"hello {now}")

