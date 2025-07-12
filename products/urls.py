from django.urls import path
from .views import product, products

urlpatterns = [
    path('', products, name='products'),
    path('product/', product, name='product'),
]