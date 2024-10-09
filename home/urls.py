from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()
