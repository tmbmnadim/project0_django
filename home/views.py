from django.shortcuts import render
from .models import SiteDetails

def homepage(request):
    site_details = SiteDetails.objects.all()
    return render(request, 'home/homepage.html', {'site_details': site_details})