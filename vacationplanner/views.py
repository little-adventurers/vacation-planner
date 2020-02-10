from django.http import HttpResponse
from django.shortcuts import render
from .models import Vacation, Itinerary

def home(request):
    vacations = Vacation.objects.all()
    return render(request, 'home.html', {'vacations': vacations})

def vacation_itinerary(request, pk):
    vacation = Vacation.objects.get(pk=pk)
    return render(request,'vacations.html',{'vacation':vacation})