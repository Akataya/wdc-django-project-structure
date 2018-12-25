from django.urls import path
from . import views


urlpatterns = [
    path('<int:prod_id>/', views.product_detail, name='product_detail'),
    path('', views.index, name='index'),
]
