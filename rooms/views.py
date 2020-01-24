# from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render
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


def room_detail(request, pk):
    return render(request, "rooms/detail.html")
