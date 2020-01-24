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
    # 나머지가 5로 떨어졌을 경우, 새로운 page에 object를 넣는 것이 아니라, 이전page에 나머지 값도 같이 표시함.
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.get_page(page)
    # print(vars(rooms.paginator))
    return render(request, "rooms/home.html", context={"page": rooms},)

