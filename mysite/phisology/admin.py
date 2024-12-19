from django.contrib import admin
from .models import *



class Consultation_keysInlines(admin.TabularInline):
    model = Consultation_Keys
    extra = 1

class KeysAdmin(admin.ModelAdmin):
    inlines = [Consultation_keysInlines]


admin.site.register(Consultation, KeysAdmin)
admin.site.register(Registration)