from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.product.models import Product
from apps.product.api.serializer import ProductSerializer
from .models import Cart, CartItem


class AddItemToCartView(APIView):
    def post(self, request, format=None):
        user = self.request.user
        data = self.request.data
        quantity = 1
        product_uuid = int(data['product_uuid'])
        try:
            if not Product.objects.filter(uuid=product_uuid).exists():
                return Response({'Error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
            product = Product.objects.get(uuid=product_uuid)
            cart = Cart.objects.get(user=user)
            if CartItem.objects.filter(cart=cart, product=product).exists():
                return Response({'Error': 'Item is already in cart.'}, status=status.HTTP_409_CONFLICT)
            if int(product.stock) > 0:
                CartItem.objects.create(product=product, cart=cart, count=quantity)
                if CartItem.objects.filter(cart=cart, product=product).exists():
                    total_items = int(cart.total_items) + 1
                    Cart.objects.filter(user=user).update(total_items=total_items)
                    cart_items = CartItem.objects.order_by('product').filter(cart=cart)
                    result = []
                    for cart_item in cart_items:
                        item = {}
                        item['id'] = cart_item.id
                        item['count'] = cart_item.count
                        product = Product.objects.get(id=cart_item.product.id)
                        product = ProductSerializer(product)
                        item['product'] = product.data
                        result.append(item)
                    return Response({'cart': result}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'Error': 'Not enough of this item in stock.'}, status=status.HTTP_200_OK)

        except:
            return Response({'Error': 'Something went wrong when adding item to cart'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
