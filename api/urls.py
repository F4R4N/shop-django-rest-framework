from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from . import views

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('user', views.UserView)
router.register('category', views.CategoryView)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="all you need to know about the shop api is in the following documentation please dont bother.",
      contact=openapi.Contact(email="farantgh@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/cart/', views.CartItemView.as_view()),
    path('v1/cart/add/', views.CartItemAddView.as_view()),
    path('v1/cart/delete/<int:pk>/', views.CartItemDelView.as_view()),
    path('v1/cart/add_one/<int:pk>/', views.CartItemAddOneView.as_view()),
    path('v1/cart/reduce_one/<int:pk>/', views.CartItemReduceOneView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui'),
]

