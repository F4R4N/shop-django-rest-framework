from rest_framework import viewsets, permissions, generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category, CartItem, Profile
from .serializers import ProductSerializer, CategorySerializer, CartItemSerializer, UserSerializer, CartItemAddSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProductView(viewsets.ModelViewSet):
    queryset = Product.available.all()
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CartItemView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)

class CartItemAddView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemAddSerializer
    permission_classes = (IsAuthenticated, )

class CartItemDelView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
