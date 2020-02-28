from django.shortcuts import render, redirect

# paginator for django
from django.core.paginator import Paginator, EmptyPage
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
    page = request.GET.get("page", 1)  # page is 1 by default

    # queryset of rooms ready as list
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#querysets-are-lazy
    room_list = models.Room.objects.all()

    # dictionary with keys of "object_list", "number", "paginator" ...
    # object_list is list of queryset, number is integer, paginator is class
    # view more methods about paginator class: https://docs.djangoproject.com/en/3.0/ref/paginator/#django.core.paginator.Paginator
    paginator = Paginator(room_list, 10, orphans=5)

    try:
        rooms_page = paginator.page(int(page))
        # print(vars(rooms_page))

        # dictionary with keys of 'per_page', 'orphans', 'allow_empty_first_page', 'count', 'num_pages'
        # print(vars(rooms_page.paginator))

        # render is telling Django "go and compile html code into browser html"
        # context is way of sending variables to html file, as {{variable}}. Logic statements go into {% if %}
        # context = {"context name": variableInViews.py}
        return render(
            request, "rooms/all_rooms.html", context={"rooms_page": rooms_page},
        )

    # exception for empty page then redirect to home
    except EmptyPage:
        return redirect("/")

