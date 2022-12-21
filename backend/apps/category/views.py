from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, SubCategory
from .api.serializer import CategorySerializer, SubCategorySerializer
from .utils import getCategoriesList, getCategoryDetail, deleteCategory


@api_view(['GET'])
def categoryRoutes(request):
    routes = [
        {
            'Endpoint': '/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of categories'
        },
        {
            'Endpoint': '/category/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single category object'
        },
        {
            'Endpoint': '/category/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete an existing category'
        },
        # {
        #     'Endpoint': '/notes/create/',
        #     'method': 'POST',
        #     'body': {'body': ""},
        #     'description': 'Creates new note with data sent in post request'
        # },
        # {
        #     'Endpoint': '/notes/id/update/',
        #     'method': 'PUT',
        #     'body': {'body': ""},
        #     'description': 'Creates an existing note with data sent in post request'
        # },

    ]
    return Response(routes)


@api_view(['GET'])
def categories(request):
    if request.method == 'GET':
        categories = Category.objects.all().order_by('-created_at')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def category(request, pk):

    if request.method == 'GET':
        return getCategoryDetail(request, pk)

    # if request.method == 'POST':
    #     return createNote(request)

    if request.method == 'DELETE':
        return deleteCategory(request, pk)


@api_view(['GET'])
def subcategories(request):
    if request.method == 'GET':
        sub_categories = SubCategory.objects.all().order_by('-created_at')
        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data)