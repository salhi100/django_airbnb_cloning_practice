from django.contrib import admin
from . import models


# http://127.0.0.1:8000/admin/conversations/message/


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    # displaying models.py fields on admin panel
    list_display = (
        "__str__",
        "created",
    )

    pass


# http://127.0.0.1:8000/admin/conversations/conversation/


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    # displaying models.py fields on admin panel
    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )

    pass
