from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    # get("page", 1) : query dictionary에서 page의 value를 가져오는 것.
    # print(request.GET.get("page", 0))
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    # Paginator(object list, page 당 object 개수)
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    print(vars(rooms.paginator))
    return render(request, "rooms/home.html", context={"rooms": rooms},)

