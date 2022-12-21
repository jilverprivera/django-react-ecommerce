from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .api.serializer import ProductSerializer


@api_view (['GET'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-created_at')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)