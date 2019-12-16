from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Vacation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='+',on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, related_name='+',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100)
    vacation = models.ForeignKey(Vacation,related_name='vacations',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.description