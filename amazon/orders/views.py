from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Browsing index page of orders")


def order(request, order_id):
    return HttpResponse(f"Details of order ID: #{order_id}")
