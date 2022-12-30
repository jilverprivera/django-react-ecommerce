from django.urls import path
from ..views import *

urlpatterns = [
    path("products/", getProducts, name='get_products'),
    path("product/<str:pk>/", getProductByID, name='get_product_by_id'),
    path("products/latest/", getLatestProducts, name='get_latest_products'),
    path("products/most-sold/", mostSoldProducts, name='most_sold_products'),
    path("products/most-stock/", mostStockProducts, name='most_stock_products'),
]
