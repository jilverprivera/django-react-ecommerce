from django.urls import path
from ..views import *

urlpatterns = [
    path("products", ProductListView.as_view()),
    path("products/latest/", NewestProductsView.as_view()),
    path("products/related/<uuid:product_uuid>/", ProductsRelatedView.as_view()),
    path("products/category/search/<uuid:category_uuid>/", SearchProductsByCategoryView.as_view()),
    path("products/search/<uuid:subcategory_uuid>/", SearchProductsBySubCategoryView.as_view()),
    path("product/<uuid:product_uuid>/", ProductView.as_view()),
]
