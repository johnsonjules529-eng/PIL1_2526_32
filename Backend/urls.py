from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription_view, name='inscription'),
    path('connexion/', views.connexion_view, name='connexion'),
    path('choix/', views.choix_view, name='choix'),
    path('profil/', views.profil_view, name='profil'),
    path('recherche/', views.recherche_mentor_view, name='recherche_mentor'),
    path('matching/', views.matching_view, name='matching'),
    path('chat/<int:destinataire_id>/', views.chat_view, name='chat'),
]