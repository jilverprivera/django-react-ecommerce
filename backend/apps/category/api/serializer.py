from rest_framework import serializers
from ..models import SubCategory, Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(source='get_absolute_url')
    image = serializers.CharField(source='get_image')
    thumbnail = serializers.CharField(source='get_thumbnail')



    class Meta:
        model = Category
        fields = (
            'uuid',
            'name',
            'slug',
            'image',
            'thumbnail',
            'created_at',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(source='get_absolute_url')
    principal = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = (
            'uuid',
            'name',
            'slug',
            'principal',
            'created_at',
        )
