from django.urls import path
from ..views import *

urlpatterns = [
    path("wishlist/", getAllUserWishlist, name="get_all_carts"),
    path("wishlist/<str:pk>/", getWishlistByUserID, name="get_all_carts"),
]
