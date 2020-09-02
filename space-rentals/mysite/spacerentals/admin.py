from django.contrib import admin

# Register your models here.

from spacerentals.models import *

admin.site.register(Pg)
admin.site.register(Booking)
admin.site.register(Review)