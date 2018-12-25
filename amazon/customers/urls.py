from django.urls import path
from . import views


urlpatterns = [
    path('/<int:customer_id>/', views.customer_info, name='customer_info'),
    path('', views.index, name='index'),
]
