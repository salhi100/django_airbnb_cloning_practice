from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def all_rooms(request):
    # check specifics of request
    # print(dir(request))

    now = datetime.now()
    # return HttpResponse(content=f"hello {now}")

    hungry = True

    # render is telling Django "go and compile html code into browser html"
    # context is way of sending variables to html file, as {{variable}}. Logic statements go into {% if %}
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})

