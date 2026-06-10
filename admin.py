from django.contrib import admin
from .models import Profil, Matiere, Matching, Message

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')

@admin.register(Matching)
class MatchingAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'mentor', 'statut', 'cree_le')
    list_filter = ('statut',)

admin.site.register(Matiere)
admin.site.register(Message)