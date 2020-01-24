from math import ceil
from django.shortcuts import render
from . import models


def all_rooms(request):
    # get("page", 1) : query dictionary에서 page의 value를 가져오는 것.
    # print(request.GET.get("page", 0))
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)

    return render(
        request,
        "rooms/home.html",
        context={
            "potato": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
