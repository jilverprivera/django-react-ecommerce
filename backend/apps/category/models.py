from django.db import models
from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    slug = models.SlugField(max_length=255, null=False, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class SubCategory(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    slug = models.SlugField(max_length=255, null=False, blank=True)
    principal = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'
        ordering = ('created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.principal.slug}/{self.slug}/'