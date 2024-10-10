from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
]