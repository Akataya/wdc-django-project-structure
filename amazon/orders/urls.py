from django.urls import path
from . import views


urlpatterns = [
    path('<int:order_id>/', views.order, name='order_info'),
    path('', views.index, name='index'),
]
