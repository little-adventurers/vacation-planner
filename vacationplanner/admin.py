from django.contrib import admin
from .models import Vacation, Itinerary, Post

# Register your models here.
admin.site.register(Vacation)
admin.site.register(Itinerary)
admin.site.register(Post)