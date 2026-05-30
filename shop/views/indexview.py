from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import Category


class IndexView(TemplateView):
    template_name = "shop/index.html"

    def get(self, request, id=None): 
        categories = Category.objects.order_by("name")
        filter = request.GET.get("q", "") #get q or empty string if not found
        if filter != "":
            title = f"Search results for '{filter}"
            products = Product.objects.filter(name__icontains=filter).order_by("name")
        elif id is not None:
            title = Category.objects.get(id=id).name
            products = Product.objects.filter(Category=id).order_by("name")
        else:
            title = "All Products"
            products = Product.objects.order_by("name")
        

        context = {
            "filter": filter,
            "title": "All Products",
            "Products": [{"id": p.id, "name": p.name, "price": p.price, "image": p.image} for p in products],
            "Categories": [{"id": c.id, "name": c.name} for c in categories]
        }

        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))