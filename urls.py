from django.urls import path
from .views import conversations_list, conversation_detail

urlpatterns = [
    path(
        "",
        conversations_list,
        name="conversations"
    ),

    path(
        "<int:conversation_id>/",
        conversation_detail,
        name="conversation_detail"
    ),
]