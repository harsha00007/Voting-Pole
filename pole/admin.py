from django.contrib import admin
from .models import Voters, Candidates

# Register your models here.
class VotersAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "mobile_number", "card_number")


admin.site.register(Voters, VotersAdmin)
admin.site.register(Candidates)