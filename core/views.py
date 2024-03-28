from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def donationCentres(request):
    return render(request, 'donationCentres.html')

def donationProcess(request):
    return render(request, 'donationProcess.html')

def events(request):
    return render(request, 'events.html')

def about(request):
    return render(request, 'about.html')

def bookingForm(request):
    form = MyForm()
    return render(request, 'bookingForm.html',{'form': form})

def emergency(request):
    return render(request, 'emergency.html')