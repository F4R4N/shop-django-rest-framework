from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
	  title="API Documentation",
	  default_version='v1',
	  description="all you need to know about the shop api is in the following documentation please dont bother.",
	  contact=openapi.Contact(email="farantgh@gmail.com"),
	  license=openapi.License(name="GPLV3 Licence", url="https://www.gnu.org/licenses/gpl-3.0.html"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
	path('admin/', admin.site.urls),
	path('v1/api/', include('api.urls')),
	path('v1/auth/', include('auth.urls')),
	path("v1/contact/", include('contactus.urls')),
	path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema_swagger_ui'),

]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
