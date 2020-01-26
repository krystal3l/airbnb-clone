# from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django_countries import countries

# from django.http import Http404
# from django.urls import reverse
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
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))

    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "instant": instant,
        "superhost": superhost,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    # room_type : fk
    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    # django queryset field lookups 참고
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#id4
    # lte : less than equal
    if price != 0:
        filter_args["price__lte"] = price

    # # greater than or equal
    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    # fk 이용.
    if superhost is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for a_amenity in s_amenities:
            filter_args["amenities__pk"] = int(a_amenity)

    if len(s_facilities) > 0:
        for f_facility in s_facilities:
            filter_args["facilities__pk"] = int(f_facility)

    rooms = models.Room.objects.filter(**filter_args)
    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})
