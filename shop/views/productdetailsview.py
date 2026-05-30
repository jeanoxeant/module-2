from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Category


class ProductDetailsView(TemplateView):
    template_name = "shop/productdetails.html"

    def get(self, request, id): 
        product = Product.objects.get(id=id)
        category = Category.objects.order_by("name")
        context = {
            "title": product.name,
            "description": product.description,
            "price": product.price,
            "volume": product.volume,
            "image": product.image,
            "category": [{"id": c.id, "name": c.name} for c in category]
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))