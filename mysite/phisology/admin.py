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