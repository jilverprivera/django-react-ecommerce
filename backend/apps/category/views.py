from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, SubCategory
from .api.serializer import CategorySerializer, SubCategorySerializer
from .utils import category_routes, getCategoriesList, getCategoryDetail, deleteCategory, subcategory_routes


@api_view(['GET'])
def categoryRoutes(request):
    return Response(category_routes(request))


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
def subcategoryRoutes(request):
    return Response(subcategory_routes(request))

@api_view(['GET'])
def getSubcategories(request, pk):
    if request.method == 'GET':
        category = Category.objects.get(id=pk)
        sub_categories = SubCategory.objects.all().filter(principal=category)
        print(sub_categories)
        # serializer = CategorySerializer(category, many=False)
        serializer = SubCategorySerializer(sub_categories, many=True)
        # print(serializer)

    # sub_categories = SubCategory.objects.all().filter(
    #     principal=category_id).order_by('-created_at')
    return Response(serializer.data)


@api_view(['GET'])
def subcategories(request):
    if request.method == 'GET':
        sub_categories = SubCategory.objects.all().order_by('-created_at')
        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data)
