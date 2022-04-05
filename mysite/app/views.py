from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product


def api_home(request, *args, **kwargs):
    data_model = Product.objects.all().order_by("?").first()
    data = {}
    if data_model:
        data["title"] = data_model.title
        data["content"] = data_model.content
        data["price"] = data_model.price
    return JsonResponse({"message": "This is a first", "product": data})
