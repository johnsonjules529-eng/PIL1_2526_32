# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from .models import Conversation, Message


def conversations_list(request):
    conversations = Conversation.objects.all()

    return render(
        request,
        "messaging/conversations.html",
        {
            "conversations": conversations
        }
    )


def conversation_detail(request, conversation_id):

    conversation = get_object_or_404(
        Conversation,
        id=conversation_id
    )

    messages = conversation.messages.order_by(
        "date_envoi"
    )

    if request.method == "POST":

        contenu = request.POST.get("contenu")

        if contenu:

            Message.objects.create(
                conversation=conversation,
                expediteur=request.user,
                contenu=contenu
            )

            return redirect(
                "conversation_detail",
                conversation_id=conversation.id
            )

    return render(
        request,
        "messaging/conversation_detail.html",
        {
            "conversation": conversation,
            "messages": messages
        }
    )