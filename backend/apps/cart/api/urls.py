from django.urls import path
from ..views import *

urlpatterns = [
    path("cart/", getAllUserCarts, name="get_all_carts"),
    path("cart/<str:pk>/", getCartByUserID, name="get_all_carts"),
]
