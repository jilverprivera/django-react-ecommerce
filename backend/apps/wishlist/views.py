from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Wishlist
from .api.serializer import WishlistSerializer

@api_view(['GET'])
def getAllUserWishlist(request):
    if request.method == 'GET':
        products = Wishlist.objects.all().order_by('-added_at')
        serializer = WishlistSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getWishlistByUserID(request, pk):
    if request.method == 'GET':
        products = Wishlist.objects.all().filter(user=pk).order_by('-added_at')
        serializer = WishlistSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
