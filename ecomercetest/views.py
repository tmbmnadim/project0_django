from django.views import generic

from .models import Product


class IndexView(generic.ListView):
    template_name = "ecomercetest/index.html"
    context_object_name = "latest_product_list"

    def get_queryset(self):
        """Get 5 Latest Products"""
        return Product.objects.order_by("-product_id")[:5]

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "ecomercetest/product_detail.html"
    context_object_name = "product"