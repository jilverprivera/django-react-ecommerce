from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from ..models import Brands, Product, Comment
from apps.category.api.serializer import SubCategorySerializer


class CommentSerializer(serializers.ModelSerializer):
    first_name = SerializerMethodField()
    full_name = SerializerMethodField()
    email = SerializerMethodField()
    user_image = SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'email',
            'first_name',
            'full_name',
            'user_image',
            'created_at',
            'star_number',
            'message',
        )

    def get_email(self, obj):
        return obj.user.email

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_full_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def get_user_image(self, obj):
        return 'http://127.0.0.1:8000' + obj.user.image.url


class BrandsSerializer(ModelSerializer):
    created_at = SerializerMethodField()
    slug = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Brands
        fields = (
            'id',
            'name',
            'slug',
            'created_at',
        )

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d-%m-%Y, %H:%M:%S')


class ProductSerializer(ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail')
    image = serializers.CharField(source='get_image')
    slug = serializers.CharField(source='get_absolute_url')
    stars = serializers.IntegerField(source='get_stars')
    total_stars = serializers.IntegerField(source='get_number_starts')
    comment = CommentSerializer(many=True)
    category = SubCategorySerializer()
    brand = BrandsSerializer()

    class Meta:
        model = Product
        fields = (
            'uuid',
            'title',
            'slug',
            'category',
            'brand',
            'short_description',
            'content',
            'price',
            'compare_price',
            'stock',
            'sold',
            'image',
            'thumbnail',
            'comment',
            'stars',
            'total_stars',
            'best_seller',
            'status',
            'created_at',
        )

    # def get_created_at(self, obj):
    #     return obj.created_at.strftime('%d-%m-%Y') #%H:%M:%S
