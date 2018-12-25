from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Browsing index page of customers")


def customer_info(request, customer_id):
    return render(request, 'customer_info.html', {
        'customer_id': customer_id,
        'first_name': 'Jane',
        'last_name': 'Smith'
    })
