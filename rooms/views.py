from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def all_rooms(request):
    # check specifics of request
    # print(dir(request))

    # now = datetime.now()
    # return HttpResponse(content=f"hello {now}")

    return render(request, "all_rooms")
