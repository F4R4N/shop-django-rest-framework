from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('user', views.UserView)
router.register('category', views.CategoryView)
router.register('cart', views.CartItemView)


urlpatterns = [
    path('v1/', include(router.urls)),
]

