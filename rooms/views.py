# Using Listview
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#listview-working-with-many-django-objects
# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/

# importing models.py and python
from django.utils import timezone

# django views, urls modules
from django.views.generic import ListView, DetailView
from django.shortcuts import render

# my app
from . import models

# third party app
from django_countries import countries


# proceed with errors
class HomeView(ListView):

    """ HomeView Definition """

    # programming class based views (not function based views)
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "page"
    # changing object_list into rooms
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context

    # # rendering redirection
    # https://stackoverflow.com/a/5433410/1136110
    # def render_to_response(self, context):
    #     if not self.videos:
    #         return get_redirect_url()

    #     return super(HomeView, self).render_to_response(context)


# class based views
# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.detail/DetailView/
class RoomDetail(DetailView):

    """" RoomDetail Definition """

    model = models.Room
    # pk_url_kwarg = "pk" # primary key as query is the default
    pass


# function based views
def search(request):

    # GET REQUESTS
    # print(request.GET)
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    # print(city)  # capitalizing since database values are capitalized
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    beds = int(request.GET.get("beds", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    # getting not only one item, but get several items in user requests
    # https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.QueryDict.getlist
    selected_amenities = request.GET.getlist("amenities")
    selected_facilities = request.GET.getlist("facilities")
    # print(selected_amenities, selected_facilities)
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))

    # user request
    form = {
        "city": city,
        "selected_room_type": room_type,
        "selected_country": country,
        "price": price,
        "guests": guests,
        "beds": beds,
        "bedrooms": bedrooms,
        "selected_amenities": selected_amenities,
        "selected_facilities": selected_facilities,
    }

    # QUERYING DATABASE
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    # querying selected choices from database
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
        "instant": instant,
        "superhost": superhost,
    }

    # refer to field lookups for querying and filtering "__lte" stuff
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
    filter_args = {}

    if city != "Anywhere":
        # adding arguments as {"city__startswith" : city}
        filter_args["city__startswith"] = city
    # adding arguments of {"country" : country}
    filter_args["country"] = country
    # room_type 0 is Entire Place
    if price != 0:
        filter_args["price__lte"] = price
    if guests != 0:
        filter_args["guests_gte"] = guests
    if bedrooms != 0:
        filter_args["bedrooms_gte"] = bedrooms
    if beds != 0:
        filter_args["beds_gte"] = beds
    if instant is True:
        filter_args["instant_book"] = True

    # filtering with foreignkey relationship with primary key
    if room_type != 0:
        filter_args["room_type__pk"] = room_type
    # accessing foreignkey is easy. "pointing fieldname"__"pointed fieldname"
    if superhost is True:
        filter_args["host__superhost"] = True
    # print(room_type, superhost)

    # FILTERS SHOULD BE ABOVE THIS LINE
    # query rooms from database that matches the filter
    # https://docs.djangoproject.com/en/2.2/topics/db/queries/#retrieving-specific-objects-with-filters
    # print(filter_args)
    rooms = models.Room.objects.filter(**filter_args)
    # print(rooms)

    # FILTERING QUERYSET OF ROOMS, WITH MULTIPLE PRIMARY KEYS
    print(selected_amenities, selected_facilities)

    if len(selected_amenities) != 0:
        for selected_amenity in selected_amenities:
            rooms = rooms.filter(amenities__pk=int(selected_amenity))
            print(rooms)

    if len(selected_facilities) != 0:
        for selected_facility in selected_facilities:
            rooms = rooms.filter(facilities__pk=int(selected_facility))
            print(rooms)

    # YOU WILL SEE REMAINDER OF FILTERED ROOMS QUERYSET
    # print(rooms)

    # RESPONSE
    return render(
        request,
        "rooms/search.html",
        # Using context, we reflect user request and queryset choices to search.html.
        # We unpack each dictionary with **, and merge back into dictionary
        context={**form, **choices, "rooms": rooms},
    )
