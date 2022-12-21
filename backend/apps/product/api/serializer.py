from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from ..models import Product, Comment
from apps.category.api.serializer import SubCategorySerializer


class CommentSerializer(serializers.ModelSerializer):
    created_at = SerializerMethodField()
    user = serializers.CharField()

    class Meta:
        model = Comment

        exclude = [
            'id', 'updated_at'
        ]

    def get_user(self, obj):
        return obj.user.first_name

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d-%m-%Y, %H:%M:%S')


class ProductSerializer(ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail')
    image = serializers.CharField(source='get_image')
    slug = serializers.CharField(source='get_absolute_url')
    stars = serializers.IntegerField(source='get_stars')
    total_stars = serializers.IntegerField(source='get_number_starts')
    comment = CommentSerializer(many=True)
    created_at = SerializerMethodField()
    updated_at = SerializerMethodField()
    category = SubCategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug',
            'category',
            'price',
            'stock',
            'sold',
            'status',
            'best_seller',
            'stars',
            'total_stars',
            'comment',
            'image',
            'thumbnail',
            'created_at',
            'updated_at'
        )

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d-%m-%Y, %H:%M:%S')

    def get_updated_at(self, obj):
        return obj.updated_at.strftime('%d-%m-%Y, %H:%M:%S')