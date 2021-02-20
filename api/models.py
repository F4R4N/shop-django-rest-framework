from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from datetime import datetime
import os


def product_image(instance, filename):
    return 'images/{0}.jpg'.format(instance.slug)


def user_images(instance, filename):
    saved_file_name = instance.user.username + "-" + datetime.now().strftime("%Y_%m_%d") + ".jpg"
    return 'profile/{0}/{1}.jpg'.format(instance.user.username, saved_file_name)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    is_lux = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super(AvailableManager, self).get_queryset().filter(is_available=True, quantity__gte=1)

class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False )
    slug = models.SlugField(unique=True, null=False, blank=False)
    category = models.ManyToManyField(Category, related_name='products')
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField()
    objects = models.Manager()
    available = AvailableManager()
    created = models.DateTimeField(auto_now_add=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image)
    description = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=user_images, default='profile/default/default.png')

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

    def get_total_price(self):
        return self.quantity * self.product.price


@receiver(post_delete, sender=Profile)
def profile_image_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(True)

@receiver(post_delete, sender=Product)
def product_image_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(True)