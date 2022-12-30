from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cart
from .api.serializer import CartSerializer


@api_view(['GET'])
def getAllUserCarts(request):
    if request.method == 'GET':
        products = Cart.objects.all().order_by('-added_at')
        serializer = CartSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getCartByUserID(request, pk):
    if request.method == 'GET':
        products = Cart.objects.all().filter(user=pk).order_by('-added_at')
        serializer = CartSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
