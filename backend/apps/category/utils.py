from rest_framework.response import Response
from .api.serializer import CategorySerializer
from .models import Category


def getCategoriesList(request):
    categories = Category.objects.all().order_by('-created_at')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


def getCategoryDetail(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    print(serializer)

    return Response(serializer.data)


def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response('Category has been deleted succesfully.')


def category_routes(request):
    routes = [
        {
            'name': 'Get all categories',
            'Endpoint': '/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of categories'
        },
        {
            'name': 'Get category by ID',
            'Endpoint': '/category/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single category object'
        },
        {
            'name': 'Create category',
            'Endpoint': '/category/create/',
            'method': 'POST',
            'body': None,
            'description': 'Create a category'
        },
        {
            'name': 'Update category',
            'Endpoint': '/category/update/id/',
            'method': 'PUT',
            'body': {'name': '', 'slug': ''},
            'description': 'Update an existing category'
        },
        {
            'name': 'Delete category',
            'Endpoint': '/category/delete/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete an existing category'
        },
    ]
    return routes


def subcategory_routes(request):
    routes = [
        {
            'name': 'Get all sub-categories',
            'Endpoint': '/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of sub-categories'
        },
        {
            'name': 'Get sub-categories by principal ID',
            'Endpoint': '/sub_categories/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a array of sub-categories'
        },
        {
            'name': 'Get sub-category by ID',
            'Endpoint': '/sub-category/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single sub-category object'
        },
        {
            'name': 'Create sub category',
            'Endpoint': '/sub_category/create/',
            'method': 'POST',
            'body': None,
            'description': 'Create a sub-category'
        },
        {
            'name': 'Update sub-category',
            'Endpoint': '/sub_category/update/id/',
            'method': 'PUT',
            'body': {'name': '', 'slug': '', 'principal': {'name': '', 'slug': ''}},
            'description': 'Update an existing sub-category'
        },
        {
            'name': 'Delete sub-category',
            'Endpoint': '/sub_category/delete/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete an existing sub-category'
        },
    ]
    return routes
