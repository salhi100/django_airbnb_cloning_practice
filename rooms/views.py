# Using Listview
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#listview-working-with-many-django-objects
# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/

# importing models.py and python
from django.utils import timezone

# django views, urls modules
from django.views.generic import ListView, DetailView
from django.shortcuts import render

# my python files
from . import models, forms

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
    form = forms.SearchForm()
    return render(request, "rooms/search.html", context={"form": form})
