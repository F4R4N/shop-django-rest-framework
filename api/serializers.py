from rest_framework import serializers
from .models import Product, Category, CartItem, Profile
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    """ serializer for categories that serialize all of the fields based on Category model"""
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """ serializer for products that serialize: \n(id', 'url', "name", "slug", "category", "price", "discount", "available", "quantity", "created", "image",
                  "description") \nand add relation to category serializer \nbased on Product model """
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'url', "name", "slug", "category", "price", "discount", "available", "quantity", "created", "image",
                  "description")

class UserSerializer(serializers.ModelSerializer):
    """ serializer for user that serialize : \n(
            'id', 'username', 'first_name', 'last_name', 'email', 'image', 'is_staff', 'is_active', 'is_superuser')\nbased on default 'User' model """
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'image', 'is_staff', 'is_active', 'is_superuser')
    image = serializers.ImageField(source='profile.image')



class CartItemSerializer(serializers.ModelSerializer):
    """ serializer for cartitem that serialize all fields in 'CartItem' class model and add 'product' as relation """
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = "__all__"

    def create(self, validated_data):
        # TODO: edit the following two line
        user = User.objects.get(self.context['request'].user.id)
        product = Product.objects.get(validated_data['product'])
        cart = CartItem.objects.create(
            product=product,
            user=user,
            quantity=validated_data['quantity']
            )

        cart.save()
        return cart
           