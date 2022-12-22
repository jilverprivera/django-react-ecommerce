from django.urls import path
from ..views import categoryRoutes, categories, category, deleteCategory, subcategories, getSubcategories, subcategoryRoutes

urlpatterns = [
    path("category/routes/", categoryRoutes, name='category-routes'),
    path('categories/', categories, name="categories"), # Get all categories.
    path('category/<str:pk>/', category, name="category"), # Get category by id.
    path('category/create/', deleteCategory, name="delete-category"), # Create category.
    path('category/update/<str:pk>/', deleteCategory, name="delete-category"), # Update category.
    path('category/delete/<str:pk>/', deleteCategory, name="delete-category"), # Delete category.

    path("sub_category/routes/", subcategoryRoutes, name='category-routes'),
    path('sub_categories/', subcategories, name="sub-categories"), # Get all sub-categories.
    path('sub_categories/<str:pk>/', getSubcategories, name="sub-categories"), # Get sub-categories by category id.
    path('sub_category/<str:pk>/', getSubcategories, name="sub_category"), # Get a single sub-category
    path('sub_category/create/', getSubcategories, name="sub_category"), # Create sub-category
    path('sub_category/update/<str:pk>/', getSubcategories, name="sub_category"), # Update sub-category
    path('sub_category/delete/<str:pk>/', getSubcategories, name="sub_category"), # Delete sub-category

]
