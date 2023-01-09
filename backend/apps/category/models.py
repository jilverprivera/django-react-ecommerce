from django.db import models
from django.core.files import File

import uuid
from io import BytesIO
from PIL import Image

from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    slug = models.SlugField(max_length=255, null=False, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='category_thumbnail/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.slug}/'

    def get_image(self):
        if self.image:
            return self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(640, 480)):
        img = Image.open(image)
        if img.mode in ["RGBA", "P"]:
            img = img.convert("RGB")
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=90)
        image_name = image.name.split('/')
        image_name=image_name[1]
        thumbnail = File(thumb_io, name=image_name)
        return thumbnail


class SubCategory(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    slug = models.SlugField(max_length=255, null=False, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    principal = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'
        ordering = ('created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.principal.slug}/{self.slug}/'

    def get_principal(self):
        return f'{self.principal.slug}'
