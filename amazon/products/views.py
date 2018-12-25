from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Browsing index page of products")


def product_detail(request, prod_id):
    return HttpResponse(f"Details of Product ID: #{prod_id}")
