# from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category, CartItem, Profile
from .serializers import ProductSerializer, CategorySerializer, CartItemSerializer, UserSerializer, CartItemAddSerializer
from django.contrib.auth.models import User
from rest_framework import generics

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CartItemView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated, )

class CartItemAddView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemAddSerializer
    permission_classes = (IsAuthenticated, )