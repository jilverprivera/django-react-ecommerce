from django.contrib import admin

from apps.category.models import Category, SubCategory

admin.site.register(Category)
admin.site.register(SubCategory)
