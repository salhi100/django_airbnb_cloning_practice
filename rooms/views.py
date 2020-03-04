# Using Listview
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#listview-working-with-many-django-objects
# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/

# importing models.py and python
from django.utils import timezone

# django views, urls modules
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render

# my python files
from . import models, forms


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


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):
        country = request.GET.get("country")

        # unbound form: form not given with some data
        # form = forms.SearchForm()

        if country:
            # give form with user's GET request
            # form validates data in Get request
            form = forms.SearchForm(request.GET)

            if form.is_valid():
                # print(form.cleaned_data)
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                room_type = form.cleaned_data.get("room_type")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                # refer to field lookups for querying and filtering
                # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#field-lookups
                # refer to field lookups for querying and filtering "__lte" stuff
                # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
                filter_args = {}

                # we can't add (default = False) to CharField at forms.py.
                # So we are using this instead
                if city != "Anywhere":
                    # adding arguments as {"city__startswith" : city}
                    filter_args["city__startswith"] = city

                # adding arguments of {"country" : country}
                filter_args["country"] = country

                # filtering with foreignkey relationship -> refer to models.py
                # room_type 0 is entire place
                # room_type 0 is Entire Place
                if price is not None:
                    filter_args["price__lte"] = price
                if guests is not None:
                    filter_args["guests__gte"] = guests
                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms
                if beds is not None:
                    filter_args["beds__gte"] = beds
                if instant_book is True:
                    filter_args["instant_book"] = True

                # Not using primary key, but just use object from database itself
                if room_type is not None:
                    filter_args["room_type"] = room_type
                # accessing foreignkey is easy. "pointing fieldname"__"pointed fieldname"
                if superhost is True:
                    filter_args["host__superhost"] = True
                # print(room_type, superhost)

                # INSTEAD OF PRIMARY KEYS,
                # Actual amenities and facilities items are retreived in cleaned data
                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                # FILTERS SHOULD BE ABOVE THIS LINE
                # query rooms from database that matches the filter
                # https://docs.djangoproject.com/en/2.2/topics/db/queries/#retrieving-specific-objects-with-filters
                print(filter_args)
                rooms = models.Room.objects.filter(**filter_args)

                # YOU WILL SEE REMAINDER OF FILTERED ROOMS QUERYSET
                print(rooms)

        else:
            # empty form without validation
            form = forms.SearchForm()

        return render(
            request, "rooms/search.html", context={"form": form, "rooms": rooms}
        )
