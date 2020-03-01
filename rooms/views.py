# Using Listview
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#listview-working-with-many-django-objects
# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.list/ListView/
from django.views.generic import ListView, RedirectView
from . import models
from django.utils import timezone
from django.shortcuts import render

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


def room_detail(request, pk):
    # receiving "localhost/rooms/110230" to use it as primary key for database
    print(pk)
    return render(request, "rooms/detail.html")
