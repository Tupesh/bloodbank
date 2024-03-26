from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('bookingForm', views.bookingForm, name='bookingForm'),
    path('donationCentres', views.donationCentres, name='donationCentres'),
    path('donationProcess', views.donationProcess, name='donationProcess'),
    path('emergency', views.emergency, name='emergency'),
    path('events', views.events, name='events'),
    path('home', views.home, name='home'),

]
