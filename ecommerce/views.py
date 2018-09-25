from django.shortcuts import render
from  django.views.generic.base import TemplateView
from django.views.generic import ListView
from products.models import Product_Category
from django.http import JsonResponse



class Home(TemplateView):

    template_name = "index.html"


def list_categories(request):

    categories_list = Product_Category.objects.all()
    categories = []
    for item in categories_list:
        categories.append(item.category)
    categories = {"categories":categories}




    return JsonResponse(categories)