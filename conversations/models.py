from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField(
        "users.User", related_name="conversation", blank=True
    )

    # __str__ : str만 가능하기때문에 join(list->str) 이용
    def __str__(self):
        username = []
        for user in self.participants.all():
            username.append(user.username)
        return ", ".join(username)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    Conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
