from django.urls import path
from ..views import categoryRoutes, categories, category, deleteCategory, subcategories

urlpatterns = [
    path("category/routes/", categoryRoutes, name='category-routes'),
    path('categories/', categories, name="categories"),
    path('category/<str:pk>/', category, name="category"),
    path('category/<str:pk>/delete/', deleteCategory, name="delete-category"),

    path('sub-categories/', subcategories, name="sub-categories"),
]
