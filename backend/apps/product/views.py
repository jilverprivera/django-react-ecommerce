from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from apps.category.models import *
from .models import Product
from .api.serializer import ProductSerializer


class ProductListView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        sort_by = request.query_params.get('sort_by')
        order = request.query_params.get('order')
        limit = request.query_params.get('limit')
        # greater_than = request.query_params.get('greater_than')
        # less_than = request.query_params.get('less_than')
        
        if not (sort_by == 'created_at' or sort_by == 'price' or sort_by == 'sold' or sort_by == 'title' or sort_by == 'stock'):
            sort_by = 'created_at'
        
        if not limit:
            limit = 20
        try:
            limit = int(limit)
        except:
            return Response({'Error': 'Limit must be an integer.'}, status=status.HTTP_404_NOT_FOUND)
        if limit <= 0:
            limit = 10
            
        if order == 'desc':
            sort_by = '-' + sort_by
            products = Product.objects.order_by(sort_by).all().filter(status="published")[:int(limit)]
        else:
            products = Product.objects.order_by(sort_by).all().filter(status="published")[:int(limit)]
        
        # if not greater_than:
        #     greater_than = 0
        # if not less_than:
        #     less_than = 1000
        # products = products.filter(price__gte=greater_than)
        # products = products.filter(price__lt=less_than)

        serialized_products = ProductSerializer(products, many=True)
        if serialized_products:
            return Response(serialized_products.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'No products in list.'}, status=status.HTTP_404_NOT_FOUND)


class NewestProductsView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        products = Product.objects.order_by('-created_at').all().filter(status="published")[:4]
        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)


class ProductView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, product_uuid,  format=None):
        if Product.objects.filter(uuid=product_uuid).exists():
            product = Product.objects.get(uuid=product_uuid)
            serialized_product = ProductSerializer(product)
            return Response(serialized_product.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Product with this uuid does not exist.'}, status=status.HTTP_404_NOT_FOUND)


class ProductsRelatedView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, product_uuid, format=None):
        if not Product.objects.filter(uuid=product_uuid).exists():
            return Response({'Error': 'Product with this uuid does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        category = Product.objects.get(uuid=product_uuid).category
        if Product.objects.filter(category=category).exists():
            products = Product.objects.order_by('-stock').filter(category=category)
            products = products.exclude(uuid=product_uuid)
            serialized_products = ProductSerializer(products, many=True)
            return Response(serialized_products.data[0:4], status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'No related products found.'}, status=status.HTTP_404_NOT_FOUND)


class SearchProductsBySubCategoryView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, subcategory_uuid, format=None):
        if SubCategory.objects.filter(uuid=subcategory_uuid).exists():
            subcategory = SubCategory.objects.get(uuid=subcategory_uuid)
            products = Product.objects.order_by('-created_at').filter(category=subcategory)
            if not products:
                return Response({'Error': 'No products found with this subcategory uuid.'}, status=status.HTTP_204_NO_CONTENT)
            serialized_products = ProductSerializer(products, many=True)
            return Response(serialized_products.data, status=status.HTTP_200_OK)
        return Response({'Error': 'No subcategory found'}, status=status.HTTP_404_NOT_FOUND)


class SearchProductsByCategoryView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, category_uuid, format=None):
        if not Category.objects.filter(uuid=category_uuid).exists():
            return Response({'Error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
        category = Category.objects.get(uuid=category_uuid)
        subcategories = SubCategory.objects.order_by('-created_at').filter(principal=category)
        for subcategory in subcategories:
            products = Product.objects.order_by('-created_at').filter(category=subcategory)
            if not products:
                pass
        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)
        # print(products)
        # return Response({'Error': 'No products found with this subcategory uuid.'}, status=status.HTTP_204_NO_CONTENT)
        # if not products:





# class ListBySearchView(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def post(self, request, format=None):
#         data = self.request.data
#         try:
#             category_id = int(data['category_id'])
#         except:
#             return Response({'Error': 'ID must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)

#         order = data['order']
#         sort_by = data['sort_by']
#         price_range = data['price_range']

#         if not (sort_by == 'created_at' or sort_by == 'price' or sort_by == 'sold' or sort_by == 'title' or sort_by == 'stock' or sort_by == 'stars'):
#             sort_by = 'created_at'

#         if category_id == 0:
#             products = Product.objects.all()
#         elif not SubCategory.objects.filter(id=category_id).exists():
#             return Response({'Error': 'Category does not exist.'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             category = SubCategory.objects.get(id=category_id)
#             if category:
#                 products = Product.objects.filter(category=category)
#         if price_range == '1 - 19':
#             products = products.filter(price__gte=1)
#             products = products.filter(price__lt=20)
#         elif price_range == '20 - 39':
#             products = products.filter(price__gte=20)
#             products = products.filter(price__lt=40)
#         elif price_range == '40 - 59':
#             products = products.filter(price__gte=40)
#             products = products.filter(price__lt=60)
#         elif price_range == '60 - 79':
#             products = products.filter(price__gte=60)
#             products = products.filter(price__lt=80)
#         elif price_range == '80 - 99':
#             products = products.filter(price__gte=80)
#             products = products.filter(price__lt=100)
#         elif price_range == 'More than 100':
#             products = products.filter(price__gte=100)

#         if order == 'desc':
#             sort_by = '-' + sort_by
#             products = products.order_by(sort_by)
#         elif order == 'asc':
#             products = products.order_by(sort_by)
#         else:
#             products = products.order_by(sort_by)

#         serialized_products = ProductSerializer(products, many=True)

#         if len(serialized_products.data) > 0:
#             return Response(serialized_products.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'Error': 'No products found.'}, status=status.HTTP_204_NO_CONTENT)
