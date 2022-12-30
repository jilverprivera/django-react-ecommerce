from django.db import models
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.category.models import SubCategory

from account.models import User



class Product(models.Model):
    status_options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=False, blank=True)
    title = models.CharField(max_length=128, blank=True, null=False)
    slug = models.SlugField(max_length=255, blank=True, null=False)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=False)
    stock = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail/'.format(title), blank=True, null=True)
    best_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.ManyToManyField("Comment", blank=True)
    stars = models.ManyToManyField('Star', blank=True)
    total_stars = models.IntegerField(default=0)
    status = models.CharField(
        max_length=16, choices=status_options, default='draft')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.category.principal.slug}/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def get_stars(self):
        ratings = self.stars.all()
        rate = 0
        for rating in ratings:
            rate += rating.star_number
        try:
            rate /= len(ratings)
        except ZeroDivisionError:
            rate = 0
        return rate

    def get_number_starts(self):
        return len(self.stars.all())

    def make_thumbnail(self, image, size=(640, 480)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)


class Star(models.Model):
    star_number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'
        ordering = ('-user',)


class Brands(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    slug = models.SlugField(max_length=255, null=False, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ('created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
