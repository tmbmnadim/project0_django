from django.shortcuts import render
from .models import SiteDetails

def homepage(request):
    site_details = SiteDetails.objects.get()
    return render(request, 'home/homepage.html', {'site_details': site_details})

def about(request):
    site_details = SiteDetails.objects.get()
    return render(request, 'home/about.html', {'site_details': site_details})

def services(request):
    site_details = SiteDetails.objects.get()
    return render(request, 'home/services.html', {'site_details': site_details})

def contact(request):
    site_details = SiteDetails.objects.get()
    return render(request, 'home/contact.html', {'site_details': site_details})