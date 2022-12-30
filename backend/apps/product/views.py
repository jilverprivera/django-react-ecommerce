from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .api.serializer import ProductSerializer


@api_view(['GET'])
def getProducts(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-created_at')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getProductByID(request, pk):
    if request.method == 'GET':
        product = Product.objects.all().filter(id=pk)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getLatestProducts(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-created_at')[0:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def mostSoldProducts(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-sold')[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def mostStockProducts(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-stock')[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
