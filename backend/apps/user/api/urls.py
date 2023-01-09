from django.urls import path
from ..views import *

urlpatterns = [
    path("cart/add-item/", AddItemToCartView.as_view())
]
