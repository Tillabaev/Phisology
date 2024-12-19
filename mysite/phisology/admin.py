from django.contrib import admin
from .models import *


class ImgInlines(admin.TabularInline):
    model = Img
    extra = 0


class ReviewAdmin(admin.ModelAdmin):
    inlines = [ImgInlines]

admin.site.register(AboutMe)
admin.site.register(MainWorld)
admin.site.register(Review,ReviewAdmin)



class Consultation_keysInlines(admin.TabularInline):
    model = Consultation_Keys
    extra = 1

class KeysAdmin(admin.ModelAdmin):
    inlines = [Consultation_keysInlines]


admin.site.register(Consultation, KeysAdmin)
admin.site.register(Registration)

