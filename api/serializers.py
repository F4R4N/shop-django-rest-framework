from rest_framework import serializers
from .models import Product, Category, CartItem
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class CategorySerializer(serializers.ModelSerializer):
    """
    serializer for categories that serialize all of the fields
    based on Category model

    """

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializer for products that serialize:
    (id', 'url', "name", "slug", "category", "price", "discount", "available",
    "quantity", "created", "image", "description")
    and add relation to category serializer \nbased on Product model

    """

    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id', 'url', "name", "slug", "category", "price", "discount",
            "available", "quantity", "created", "image", "description")


class UserSerializer(serializers.ModelSerializer):
    """
    serializer for user that serialize :
    ('id', 'username', 'first_name', 'last_name', 'email', 'image',
    'is_staff', 'is_active', 'is_superuser')\nbased on default 'User' model

    """

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'image',
            'is_staff', 'is_active', 'is_superuser')

    image = serializers.ImageField(source='profile.image', required=False)


class CartItemSerializer(serializers.ModelSerializer):
    """
    serializer for cartitem that serialize all fields in 'CartItem' class
    model and add 'product' as relation

    """

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'quantity', 'product')


class CartItemAddSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ('quantity', 'product_id')
        extra_kwargs = {
            'quantity': {'required': True},
            'product_id': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.get(id=self.context['request'].user.id)
        product = get_object_or_404(Product, id=validated_data['product_id'])
        if product.quantity == 0 or product.is_available is False:
            raise serializers.ValidationsError(
                {'not available': 'the product is not available.'})

        cart_item = CartItem.objects.create(
            product=product,
            user=user,
            quantity=validated_data['quantity']
            )
        cart_item.save()
        cart_item.add_amount()
        product.quantity = product.quantity - cart_item.quantity
        product.save()
        return cart_item
