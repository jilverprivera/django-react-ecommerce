from django.db import models
from io import BytesIO
from PIL import Image
import uuid

from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.category.models import SubCategory

from account.models import User


class Brands(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    slug = models.SlugField(max_length=255, null=False, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ('created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    status_options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=128, blank=True, null=False)
    slug = models.SlugField(max_length=255, blank=True, null=False)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False, blank=True)
    brand = models.ForeignKey(Brands, default=None, on_delete=models.CASCADE, null=False, blank=True)
    short_description = models.TextField(max_length=255, blank=True, null=False)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=False)
    compare_price = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=False)
    stock = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='product_thumbnail/', blank=True, null=True)
    comment = models.ManyToManyField("Comment", blank=True)
    total_stars = models.IntegerField(default=0)
    best_seller = models.BooleanField(default=False)
    status = models.CharField(max_length=16, choices=status_options, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}'

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
        # print(image_name)
        thumbnail = File(thumb_io, name=image_name)
        return thumbnail

    def get_stars(self):
        ratings = self.comment.all()
        rate = 0
        for rating in ratings:
            rate += rating.star_number
        try:
            rate /= len(ratings)
        except ZeroDivisionError:
            rate = 0
        return rate

    def get_number_starts(self):
        return len(self.comment.all())


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star_number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)


