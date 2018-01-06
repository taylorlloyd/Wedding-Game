from django.contrib import admin
from wgserver.models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'rfid_token')
admin.site.register(Player, PlayerAdmin)
