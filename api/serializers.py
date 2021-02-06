from rest_framework import serializers
from .models import Product, Category, CartItem, Profile
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'url', "name", "slug", "category", "price", "discount", "available", "quantity", "created", "image",
                  "description")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'image', 'is_staff', 'is_active', 'is_superuser')
    image = serializers.ImageField(source='profile.image')



class CartItemSerializer(serializers.ModelSerializer):
    user = ProductSerializer(many=True)
    class Meta:
        model = CartItem
        fields = "__all__"

    def create(self, validated_data):
        cart = CartItem.objects.create(
            product=validated_data['product'],
            user=validated_data['user'],
            quantity=validated_data['quantity']
            )
        cart.save()
        return cart


            