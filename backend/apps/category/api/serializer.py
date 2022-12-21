from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from ..models import Category


class CategorySerializer(ModelSerializer):
    created_at = SerializerMethodField()
    updated_at = SerializerMethodField()
    slug = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at'
        )

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d-%m-%Y, %H:%M:%S')

    def get_updated_at(self, obj):
        return obj.updated_at.strftime('%d-%m-%Y, %H:%M:%S')


class SubCategorySerializer(ModelSerializer):
    created_at = SerializerMethodField()
    updated_at = SerializerMethodField()
    slug = serializers.CharField(source='get_absolute_url')
    principal = CategorySerializer()
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'principal',
            'created_at',
            'updated_at'
        )

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d-%m-%Y, %H:%M:%S')

    def get_updated_at(self, obj):
        return obj.updated_at.strftime('%d-%m-%Y, %H:%M:%S')
