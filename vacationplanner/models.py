from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

# Create your models here.
class Vacation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='+',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    #overload the get_absolute_url method to account for UUID
    def get_absolute_url(self):
        return reverse('vacation_itineraries', args=[str(self.id)])

class Itinerary(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100)
    vacation = models.ForeignKey(Vacation,related_name='itineraries',on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    #overload the get_absolute_url method to account for UUID
    def get_absolute_url(self):
        return reverse('vacation_itineraries', args=[str(self.id)])

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='+',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment

    #overload the get_absolute_url method to account for UUID
    def get_absolute_url(self):
        return reverse('vacation_itineraries', args=[str(self.id)])