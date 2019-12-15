from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Itinerary(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Vacation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    guest = models.ManyToManyField(User,related_name='guests')
    itinerary = models.ForeignKey(Itinerary,related_name='itineraries',on_delete=models.SET)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='vacations',on_delete=models.SET)
    updated_by = models.ForeignKey(User, related_name='+',on_delete=models.SET)

    def __str__(self):
        return self.name