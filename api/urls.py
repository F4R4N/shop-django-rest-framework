from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('user', views.UserView)
router.register('category', views.CategoryView)



urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/cart/', views.CartItemView.as_view()),
    path('v1/cart/add/', views.CartItemAddView.as_view()),
    path('v1/cart/delete/<int:pk>/', views.CartItemDelView.as_view()),
    path('v1/cart/add_one/<int:pk>/', views.CartItemAddOneView.as_view()),
    path('v1/cart/reduce_one/<int:pk>/', views.CartItemReduceOneView.as_view()),
]

