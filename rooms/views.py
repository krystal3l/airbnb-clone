# from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


# class based view 참고 사이트
# http://ccbv.co.uk/


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    aginate_orphans = 5
    context_object_name = "rooms"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     now = timezone.now()
    #     context["now"] = now
    #     return context


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


"""
# FBV(function based view)
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()
"""


def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
