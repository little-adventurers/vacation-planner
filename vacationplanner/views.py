from django.http import HttpResponse
from django.shortcuts import render
from .models import Vacation, Itinerary, Post

def home(request):
    vacations = Vacation.objects.all()
    return render(request, 'home.html', {'vacations': vacations})

def vacation_itineraries(request, pk):
    vacation = Vacation.objects.get(pk=pk)
    return render(request,'itinerary.html',{'vacation':vacation})