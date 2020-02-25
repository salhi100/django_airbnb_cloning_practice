# importing django default models as class
from django.db import models

# importing Core Application's models as class
from core import models as core_models  # "as" is like "import pandas as pd"


# http://127.0.0.1:8000/admin/conversations/conversation/
class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        # giving queryset of all participants for conversations
        for user in self.participants.all():
            usernames.append(user.username)
        # return str(self.created)  # forcing datetime object into string
        return ", ".join(usernames)  # join items in the list, create long string

    # because class Message has foreign key for convesation & related name "messages", we can use variable messages
    def count_messages(self):
        return self.messages.count()

    # changing the name of count_messages into "Number of Messages" on admin panel
    count_messages.short_description = "Number of Messages"

    # because class Message has foreign key for convesation & related name "messages", we can use variable messages
    def count_participants(self):
        return self.participants.count()

    # changing the name of count_participants into "Number of participants" on admin panel
    count_participants.short_description = "Number of participants"


# http://127.0.0.1:8000/admin/conversations/message/
class Message(core_models.TimeStampedModel):

    message = models.TextField()

    # related name = "messages" allows conversation to use the variable
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
