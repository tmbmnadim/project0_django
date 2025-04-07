from django.urls import path

from . import views

app_name = "ecomercetest"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
]