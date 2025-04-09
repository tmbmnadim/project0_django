from django.views import generic

from .models import Product


class IndexView(generic.ListView):
    template_name = "ecomercetest/index.html"
    context_object_name = "latest_product_list"

    def get_queryset(self):
        """Get 5 Latest Products"""
        return Product.objects.order_by("-id")[:5]

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "ecomercetest/product_detail.html"
    context_object_name = "product"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["similar_product_list"] = Product.objects.exclude(id=self.object.id)[:5]
        return context