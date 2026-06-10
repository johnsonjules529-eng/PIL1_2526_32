# Create your models here.
from django.db import models
from accounts.models import User
from mentorat.models import Mentorat


class Conversation(models.Model):
    mentorat = models.ForeignKey(
        Mentorat,
        on_delete=models.CASCADE,
        related_name='conversations'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    messages_avant_validation = models.IntegerField(
    default=3
)
    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    expediteur = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    contenu = models.TextField()

    date_envoi = models.DateTimeField(auto_now_add=True)

    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.expediteur.username}"