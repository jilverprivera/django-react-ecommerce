from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.product.api.serializer import ProductSerializer
from ..models import Cart


class CartSerializer(ModelSerializer):
    added_at = SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'product',
            "quantity",
            'added_at',
        )

    def get_added_at(self, obj):
        return obj.added_at.strftime('%d-%m-%Y, %H:%M:%S')
