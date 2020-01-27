# from django.utils import timezone

from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# from django.http import Http404
# from django.urls import reverse
from . import models, forms


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


class SearchView(View):
    def get(self, request):
        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)  # search.html에서 전송한 form data가 저장됨

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")
                paginator = Paginator(qs, 2)
                page = request.GET.get("page")
                rooms = paginator.get_page(page)

                r_get_copy = request.GET.copy()
                address = r_get_copy.urlencode()

                return render(
                    request,
                    "rooms/search.html",
                    {"form": form, "rooms": rooms, "address": address},
                )

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form})
